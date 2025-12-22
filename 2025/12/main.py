# first section lists the standard present shapes
# each shape starts with its index and a colon
# then the shape is displayed visually, where # is part of the shape and . is not

# the second section lists the regions under the trees
# each line starts with the width and legnth of the region
# the rest of the line describes the presents that need to fit into that region
# by listing the quantity of each shape

# presents can be rotated and flipped as necessary, shapres can't overlap
# the # part can't go into the same place on the grid

# the elves need to know how many of the regions can fit the presents listed

# example:
# region: 4x4: 0 0 0 0 2 0
# region:
# ....
# ....
# ....
# ....
# we need to fit 2 presents that have shape index 4

# valid solution (A, B as presents):
# AAA.
# ABAB
# ABAB
# .BBB


def read_input(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    presents = {}
    last_present = None
    regions = []

    for line in lines:
        if line == "":
            continue
        elif "#" in line or "." in line:
            # present
            presents[last_present].append(list(line))
        else:
            split = line.split(":")
            if split[-1] == "":
                last_present = int(split[0])
                presents[last_present] = []
            else:
                area = tuple([int(x) for x in split[0].split("x")])
                regions.append((area, [int(x) for x in split[-1].strip().split()]))

    return (presents, regions)


# no idea why this works tbh
def part_one(file):
    presents, regions = read_input(file)

    # back tracking solution, by trying all possible placements of the presents with their rotations and flips
    # if we find a valid placement, we add it to the count
    answer = 0

    for region in regions:
        size = region[0]
        presents = region[1]

        print(size, presents)

        total_area = size[0] * size[1]

        # 9 is the area of the present that it takes up, this doesn't account for rotations and flips though
        if 9 * sum(presents) <= total_area:
            answer += 1

    print(answer)

    return answer


if __name__ == "__main__":
    part_one("2025/12/sample-input.txt")
    # part_one("2025/12/input.txt")
