# fresh and spoiled ingredients
# database operates on ingredient IDs
# list of fresh, a blank line, tthen a list of available IDs
# fresh IDs are inclusive
# ranges can overlap, an ingredient is fresh if it is in any range


def read_input(file):
    with open(file) as f:
        return f.read().splitlines()


def part_one(file):
    database = read_input(file)

    fresh_count = 0
    # split the database into fresh and available
    blank_index = database.index("")

    fresh = database[:blank_index]
    available = database[blank_index + 1 :]

    fresh = [range(int(x.split("-")[0]), int(x.split("-")[1]) + 1) for x in fresh]
    available = [int(x) for x in available]

    for ingredient in available:
        for fresh_range in fresh:
            if ingredient in fresh_range:
                fresh_count += 1
                break

    return fresh_count


# count the ranges instead
def part_two(file):
    database = read_input(file)

    count = 0
    # split the database into fresh and available
    blank_index = database.index("")

    fresh = database[:blank_index]
    # available = database[blank_index + 1 :]

    fresh = [range(int(x.split("-")[0]), int(x.split("-")[1]) + 1) for x in fresh]

    # sort and merge ranges
    fresh.sort(key=lambda x: x.start)
    merged = []
    for fresh_range in fresh:
        if merged and merged[-1].stop >= fresh_range.start:
            merged[-1] = range(merged[-1].start, max(merged[-1].stop, fresh_range.stop))
        else:
            merged.append(fresh_range)

    fresh = merged

    for fresh_range in fresh:
        count += fresh_range.stop - fresh_range.start

    return count


if __name__ == "__main__":
    print("part_one:", part_one("05/input.txt"))
    print("part_two:", part_two("05/input.txt"))
