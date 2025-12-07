# each problem's numbers are arranged vertically
# grand total is adding each problem up

import math


def parse_input(file: str):
    with open(file) as f:
        lines = f.read().splitlines()

        # split each line into a list of strings separated by space
        lines = [line.split() for line in lines]

        # split it into the numbers and the operators
        numbers = [[int(x) for x in line if x.isdigit()] for line in lines[:-1]]
        operators = lines[-1]
        return (numbers, operators)


def part_one(file: str):
    (numbers, operators) = parse_input(file)
    grand_total = 0

    # get the numbers in the columns
    for operator_index in range(len(operators)):
        operator = operators[operator_index]
        problem_numbers = [row[operator_index] for row in numbers]

        if operator == "+":
            grand_total += sum(problem_numbers)
        elif operator == "*":
            grand_total += math.prod(problem_numbers)

    return grand_total


def parse_right_to_left(file: str):
    with open(file) as f:
        lines = f.read().splitlines()

        # The last line contains the operators and defines the column positions
        operators_line = lines[-1]
        operators = operators_line.split()

        # Determine start indices of columns based on non-space characters in operator line
        col_lens = [i for i, char in enumerate(operators_line) if char != " "]
        numbers_lines = lines[:-1]

        new_lines = []
        # split on the indices of col_lens instead and
        # pad with zeros on the correct side of each number
        for i in range(len(numbers_lines)):
            n = []
            for j in range(len(col_lens)):
                if j >= len(col_lens) - 1:
                    n.append(numbers_lines[i][col_lens[j] :].replace(" ", "0"))
                else:
                    n.append(
                        numbers_lines[i][col_lens[j] : col_lens[j + 1] - 1].replace(
                            " ", "0"
                        )
                    )
            new_lines.append(n)

        return (new_lines, operators)


# the numbers need to be read from right to left in columns instead
def part_two(file: str):
    (numbers, operators) = parse_right_to_left(file)
    grand_total = 0

    # get the numbers in the columns
    for operator_index in range(len(operators)):
        operator = operators[operator_index]
        problem_numbers = [row[operator_index] for row in numbers]

        # find the longest number of the problem numbers
        longest_length = max(len(x) for x in problem_numbers)
        # go column by column
        values = []
        for column in range(longest_length):  # 0, 1, 2
            nums = []
            for x in problem_numbers:
                if x[column] != "0":
                    nums.append(x[column])
            values.append(int("".join(nums)))

        if operator == "+":
            # print("problem answer: ", sum(values))
            grand_total += sum(values)
        elif operator == "*":
            # print("problem answer: ", math.prod(values))
            grand_total += math.prod(values)

    return grand_total


if __name__ == "__main__":
    print("part_one:", part_one("2025/06/input.txt"))
    print("part_two:", part_two("2025/06/input.txt"))
