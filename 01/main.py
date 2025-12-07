# around the dial are numbers 0 through 99

# input: one per line sequence of rotations
# L - left
# R - right
# distance - how many clicks to rotate the dial

# ex dial at 11, rotation of R8 would result in dial at 19 (11 + 8 = 19)
# rotation of L19 would result in dial at 0 (19 - 19 = 0)

# dial is a circle, so left from 0 is 99 and right from 99 is 0
# 5, L10 -> 95, R5 -> 0
# dial starts at 50

# actual password is the # of times the dial is left poiting at 0 after any rotation in the sequence


def read_input(file):
    with open(file, "r") as file:
        return file.readlines()


def part_one(file):
    dial = 50
    times_zero = 0

    instructions = read_input(file)

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        # left is -, right is +
        if direction == "L":
            dial = (dial - distance) % 100
        else:
            dial = (dial + distance) % 100

        if dial == 0:
            times_zero += 1

    return times_zero


def part_two(file):
    dial = 50
    times_zero = 0

    instructions = read_input(file)

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == "L":
            # how many times the distance is a multiple of 100 in the negative direction
            distance *= -1
            wraps = distance // -100
            times_zero += wraps

            next_dial = (
                distance % -100
            )  # get the number between 0 and -99, where the dial would land if it were to move that distance
            if dial != 0 and dial + next_dial <= 0:
                times_zero += 1
        else:
            # how many times the distance is a multiple of 100 in the positive direction
            wraps = distance // 100
            times_zero += wraps

            next_dial = distance % 100
            if dial + next_dial >= 100:
                times_zero += 1

        dial = (dial + distance) % 100
        # print("dial:", dial)
    return times_zero


if __name__ == "__main__":
    print("part_one:", part_one("01/input.txt"))  # 984

    print("part_two:", part_two("01/input.txt"))  # 5657
