# joltage requirements for each machine
# the manual describes one machine per line
# each line describes: single indicator light diagram in [square brackets]
# one or more button wiring schematics in (parentheses) and joltage requirements in {curly braces}

# to start a machine, its indicator lights must match those shown in the diagram
# . - off, # - on

# analyze each machine's indicator light diagram and button wiring schematics
# what is the fewest button presses required to correctly configure the indicator lights on all of the machines?


from collections import deque
from z3 import Optimize, Int, sat

import re


def parse_buttons(button_string):
    matches = re.findall(r"\((.*?)\)", button_string)

    # Iterate through the matches and convert each string into a tuple of integers
    list_of_tuples = []
    for match in matches:
        # Split the string by the comma (if it exists), then convert each part to an integer
        # The strip() removes any potential whitespace around the numbers
        tuple_elements = tuple(int(x.strip()) for x in match.split(","))
        list_of_tuples.append(tuple_elements)

    return list_of_tuples


def read_input(file):
    with open(file) as f:
        schematics = []
        lines = f.read().splitlines()
        for line in lines:
            # handle square brackets
            start = line.find("[")
            end = line.find("]")

            # handle curly braces
            start_brace = line.find("{")
            end_brace = line.find("}")

            # handle buttons
            start_button = end + 2
            end_button = start_brace - 1
            buttons = parse_buttons(line[start_button:end_button])

            schematics.append(
                (
                    line[start + 1 : end],
                    buttons,
                    line[start_brace + 1 : end_brace],
                )
            )
        return schematics


def part_one(file):
    schematics = read_input(file)

    total = 0

    for schematic in schematics:
        diagram, buttons, _ = schematic

        # is there a trick to finding the fewest button presses? or do we need to check all of them?

        # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1)
        # 0 - off, 1 - on, 2 - on, 3 - off

        # initial state = [....], goal state = [.##.]

        # we can do a bfs for this?
        initial_state = tuple([0] * len(diagram))
        expected_state = tuple([1 if x == "#" else 0 for x in diagram])

        seen = set([initial_state])

        queue = deque()
        queue.append((initial_state, 0))  # store current state, number of presses

        while len(queue):
            state, presses = queue.popleft()
            # print(state, presses)

            if state == expected_state:
                total += presses
                # print(total)
                break

            for button_option in buttons:
                new_state = list(state)
                # print(button_option)
                for index in button_option:
                    new_state[index] = 0 if new_state[index] == 1 else 1

                new_state = tuple(new_state)
                if new_state in seen:
                    continue

                seen.add(new_state)
                queue.append((new_state, presses + 1))

    return total


# each machine needs to be configured to exactly the specified joltage levels
# the machines have a set of numeric counters tracking its joltage levels
# initially all set to 0

# buttons now increase the joltage level of the index by 1
# we can push each button as many times as we want
# again find the fewest total button presses


# integer linear programming with z3
# model this problem as a system of linear equations
def part_two(file):
    schematics = read_input(file)
    total_presses = 0

    for schematic in schematics:
        _, buttons, joltage_string = schematic
        targets = [int(x.strip()) for x in joltage_string.split(",")]

        opt = Optimize()

        # Create a variable for the number of times each button is pressed
        # Constraints: Must be non-negative integers
        press_counts = [Int(f"btn_{i}") for i in range(len(buttons))]
        for p in press_counts:
            opt.add(p >= 0)

        # For each counter (joltage requirement), the sum of contributions from
        # all buttons must equal the target value.
        num_counters = len(targets)
        for i in range(num_counters):
            # Find all buttons that affect this counter index 'i'
            contributions = []
            for btn_idx, btn_targets in enumerate(buttons):
                if i in btn_targets:
                    # Each press increases the counter by 1
                    contributions.append(press_counts[btn_idx])

            if contributions:
                opt.add(sum(contributions) == targets[i])
            else:
                # If no button affects this counter, and we need a non-zero value, it's impossible
                if targets[i] != 0:
                    opt.add(1 == 0)  # Impossible constraint

        # Objective: Minimize the total number of button presses
        opt.minimize(sum(press_counts))

        if opt.check() == sat:
            model = opt.model()
            machine_total = sum(model[p].as_long() for p in press_counts)
            total_presses += machine_total
        else:
            print(f"No solution found for machine with targets {targets}")

    return total_presses


if __name__ == "__main__":
    print(part_one("2025/10/sample-input.txt"))
    print(part_one("2025/10/input.txt"))
    print(part_two("2025/10/sample-input.txt"))
    print(part_two("2025/10/input.txt"))
