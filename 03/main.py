# joltage rating, number between 1 to 9

# 987654321111111 - 98
# 811111111111119 - 89
# 234234234234278 - 78
# 818181911112111 - 92

# within each bank(line), we need to turn on exactly 2 batteries
# joltage produced is equal to the number formed by the digits on the batteries that are turned on

# ex, bank 12345, turning on 2nd and 4th batteries, produces a joltage of 24

# find the largest possible joltage each bank can product, no rearranging is allowed

# total joltage is the sum of the largest joltage of each bank


def read_input(file):
    with open(file, "r") as file:
        return file.read().splitlines()


def part_one(file):
    banks = read_input(file)
    total_joltage = 0
    for bank in banks:
        # find the max in a line exlcuding the last digit
        max_in_line = (bank[0], 0)
        for i in range(1, len(bank) - 1):
            if bank[i] > max_in_line[0]:
                max_in_line = (bank[i], i)

        # now that we have the max, we need to turn on the batteries at the index and the index + 1
        # find the max in the line after the index
        max_in_line_after = (bank[max_in_line[1] + 1], max_in_line[1] + 1)
        for i in range(max_in_line[1] + 1, len(bank)):
            if bank[i] > max_in_line_after[0]:
                max_in_line_after = (bank[i], i)

        total_joltage += int(bank[max_in_line[1]] + bank[max_in_line_after[1]])
    return total_joltage


# turn on exactly 12 batteries within each bank
def part_two(file):
    banks = read_input(file)
    total_joltage = 0
    for bank in banks:
        max_batteries = []
        start_index = 0
        # keep finding maxes in a loop 12 times
        for i in range(12):
            # start at the beginning of the bank and find the max battery digit
            max_battery = (bank[start_index], start_index)
            for j in range(start_index, len(bank) - (11 - i)):
                if bank[j] > max_battery[0]:
                    max_battery = (bank[j], j)

            max_batteries.append(max_battery)
            start_index = max_battery[1] + 1
            # print("max batteries:", len(max_batteries), max_batteries, "start index:", start_index)
        print(
            "bank:",
            bank,
            "joltage:",
            int("".join([str(battery[0]) for battery in max_batteries])),
        )
        total_joltage += int("".join([str(battery[0]) for battery in max_batteries]))

    return total_joltage


if __name__ == "__main__":
    print("part_one:", part_one("03/input.txt"))
    print("part_two:", part_two("03/input.txt"))
