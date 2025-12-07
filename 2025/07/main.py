# tachyon beam enters at S
# always moves downward
# can freely move through empty space .
# if the beam encounters a ^, then it stops and splits
# from the immediate left and right of the splitter ^

# count the number of times the beam splits

# keep track the beams and use that to pass through the row
# when encountering a splitter, update the beams, drop duplicates and count splits


def read_input(file):
    with open(file) as f:
        return [line.strip() for line in f]


def part_one(file):
    rows = read_input(file)
    beams = set()
    splits = 0
    for row in rows:
        beams_in_row = set()
        for i in range(len(row)):
            if row[i] == "S":
                beams_in_row.add((i))
            # encounter a splitter
            elif row[i] == "^" and i in beams:
                beams_in_row.add((i - 1))
                beams_in_row.add((i + 1))
                splits += 1
            elif i in beams:
                beams_in_row.add((i))

        beams = beams_in_row

    return splits


# we want to count all the different timelines instead of the splits
# each timeline is when the beam reaches the bottom of the grid
def part_two(file):
    rows = read_input(file)
    height = len(rows)
    width = len(rows[0])

    # Find start
    start_col = -1
    for c in range(width):
        if rows[0][c] == "S":
            start_col = c
            break

    if start_col == -1:
        return 0

    memo = {}

    def dfs(r, c):
        # If we fell off the sides, this path dies
        if c < 0 or c >= width:
            return 0

        # If we successfully went past the last row, we found a timeline
        if r == height:
            return 1

        state = (r, c)
        if state in memo:
            return memo[state]

        current_char = rows[r][c]
        count = 0

        if current_char == "^":
            # Split: left and right
            count = dfs(r + 1, c - 1) + dfs(r + 1, c + 1)
        else:
            # Continue straight down (. or S or anything else not ^)
            count = dfs(r + 1, c)

        memo[state] = count
        return count

    return dfs(0, start_col)


if __name__ == "__main__":
    print("part one:", part_one("2025/07/input.txt"))
    print("part two:", part_two("2025/07/input.txt"))
