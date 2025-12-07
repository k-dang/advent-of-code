# Day 4

# Rolls of paper @ are arranged on a large grid
# The forklifts can only access a roll of paper if there are
# fewer than 4 rollbs of paper in the eight adjacent cells


def parse_input(file):
    with open(file, "r") as file:
        return [list[str](row) for row in file.read().splitlines()]


directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def part_one(file):
    grid = parse_input(file)
    total_rolls = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # check the 8 directions around the cell, careful not to go out of bounds
            if grid[i][j] == "@":
                rolls_around = 0
                for direction in directions:
                    new_row = i + direction[0]
                    new_col = j + direction[1]
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[i]):
                        if grid[new_row][new_col] == "@":
                            rolls_around += 1
                if rolls_around < 4:
                    total_rolls += 1

    return total_rolls


# once a roll is accessed, it can be removed
# once a roll is removed, the forklifts can access more


def find_rolls_to_remove(grid):
    rolls_to_remove = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                rolls_around = 0
                for direction in directions:
                    new_row = i + direction[0]
                    new_col = j + direction[1]
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[i]):
                        if grid[new_row][new_col] == "@":
                            rolls_around += 1
                if rolls_around < 4:
                    rolls_to_remove.append((i, j))
    return rolls_to_remove


def remove_rolls(grid, rolls_to_remove):
    for roll in rolls_to_remove:
        grid[roll[0]][roll[1]] = "."
    return grid


def part_two(file):
    grid = parse_input(file)
    total_rolls = 0

    # keep looping over the grid and make updates to the grid
    # get the rolls that can be removed then remove then and re run
    while True:
        # if no rolls can be removed, break
        rolls_to_remove = find_rolls_to_remove(grid)
        if len(rolls_to_remove) == 0:
            break
        grid = remove_rolls(grid, rolls_to_remove)
        total_rolls += len(rolls_to_remove)

    return total_rolls


if __name__ == "__main__":
    print("part_one:", part_one("2025/04/input.txt"))
    print("part_two:", part_two("2025/04/input.txt"))
