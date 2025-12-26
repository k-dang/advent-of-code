def read_input(file_path):
    with open(file_path, "r") as file:
        left_list = []
        right_list = []

        for line in file.readlines():
            values = line.split()
            left = int(values[0])
            right = int(values[1])
            left_list.append(left)
            right_list.append(right)

        return (left_list, right_list)


# pair up the numbers
# smallest number in the left list with the smallest number in the right list
# then the second smallest left number with the second smallest right number and so on
# add up all the distances
def part_one(file_path):
    left_list, right_list = read_input(file_path)

    # sort the lists
    left_list.sort()
    right_list.sort()

    # calculate distances
    distances = [abs(left - right) for left, right in zip(left_list, right_list)]

    print(sum(distances))

    return sum(distances)


# figure out exactly how often each number from the left list appears in the right list
# calculate the total similarity score: adding up each number in the left list after multiplying it by the number of times it appears in the right list
def part_two(file_path):
    left_list, right_list = read_input(file_path)

    similarity_scores = 0
    for num in left_list:
        similarity_scores += num * right_list.count(num)

    print(similarity_scores)


if __name__ == "__main__":
    part_one("2024/01/sample-input.txt")
    part_one("2024/01/input.txt")

    part_two("2024/01/sample-input.txt")
    part_two("2024/01/input.txt")
