# each line gives the name of a device followed by a list of the devices to which it's outputs are attached.
# bbb: ddd eee, means device bbb has 2 outputs, ddd and eee
# data can't flow backwards

# start with the device labled "you"
# find every path from "you" to "out"
# count the total of different paths


import functools


def read_input(file):
    with open(file, "r") as f:
        return [line.strip().split(": ") for line in f]


# model this as a graph problem and use dfs to find all paths from "you" to "out"
def part_one(file):
    devices = read_input(file)

    adjacency_list = {}
    for device in devices:
        name, outputs = device
        adjacency_list[name] = outputs.split(" ")

    def dfs(current):
        if current == "out":
            return 1
        count = 0
        for output in adjacency_list[current]:
            count += dfs(output)
        return count

    return dfs("you")


# the problematic data path passes through both dac and fft
# find every path from svr to out that passes through both dac and fft
# find all paths that lead from svr to out then check if they pass through dac and fft
def part_two(file):
    devices = read_input(file)
    adjacency_list = {}
    for device in devices:
        name, outputs = device
        adjacency_list[name] = outputs.split(" ")

    @functools.cache
    def dfs(current, has_dac, has_fft):
        if current == "out":
            if has_dac and has_fft:
                return 1
            return 0
        count = 0
        for output in adjacency_list[current]:
            count += dfs(output, has_dac or "dac" in output, has_fft or "fft" in output)
        return count  

    return dfs("svr", False, False)


if __name__ == "__main__":
    print(part_one("2025/11/sample-input.txt"))
    print(part_one("2025/11/input.txt"))

    print(part_two("2025/11/sample-input-2.txt"))
    print(part_two("2025/11/input.txt"))
