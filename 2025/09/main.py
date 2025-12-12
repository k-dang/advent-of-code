# find the largest rectangle that uses red tiles for 2 of it's opposite corners
# our input is of where the red tiles are located in the grid

# 0 indexed grid as well
# first number is column, second is row
def read_input(input_file):
    with open(input_file) as f:
        return [[int(x) for x in line.split(",")] for line in f.read().splitlines()]


def get_area(corner1, corner2):
    return (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)


def part_one(input_file):
    data = read_input(input_file)

    # I think we can try every possible pair of corners and see which one is the largest
    max_area = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            area = get_area(data[i], data[j])
            if area > max_area:
                max_area = area

    return max_area


def is_valid_rectangle(c1, c2, edges):
    """
    Checks if a rectangle defined by corners c1 and c2 is valid inside the polygon.
    A rectangle is valid if:
    1. No polygon edge passes through its interior.
    2. Its center is inside the polygon.
    """
    x1, x2 = min(c1[0], c2[0]), max(c1[0], c2[0])
    y1, y2 = min(c1[1], c2[1]), max(c1[1], c2[1])

    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    # 1. Intersection Check:
    # If any polygon edge cuts strictly through the rectangle, it's invalid.
    for v_start, v_end in edges:
        if v_start[0] == v_end[0]:  # Vertical Polygon Edge
            vx = v_start[0]
            vy_min, vy_max = min(v_start[1], v_end[1]), max(v_start[1], v_end[1])
            # Check if vertical edge X is strictly inside rectangle X range
            if x1 < vx < x2:
                # Check if Y ranges overlap
                if max(y1, vy_min) < min(y2, vy_max):
                    return False
        else:  # Horizontal Polygon Edge
            vy = v_start[1]
            vx_min, vx_max = min(v_start[0], v_end[0]), max(v_start[0], v_end[0])
            if y1 < vy < y2:
                if max(x1, vx_min) < min(x2, vx_max):
                    return False

    # 2. Interior Check (Ray Casting):
    # Check if the rectangle's center is inside the polygon.
    inside = False
    for v_start, v_end in edges:
        # Ray casting against vertical edges
        if v_start[0] == v_end[0]:
            vx = v_start[0]
            vy_min, vy_max = min(v_start[1], v_end[1]), max(v_start[1], v_end[1])

            # Check edge is to the right of point
            if vx > mid_x:
                # Check point Y is within edge Y range
                if vy_min <= mid_y < vy_max:
                    inside = not inside

    return inside


# our rectangle can include red or green tiles as well
# in our list every red tile is connected to the red tile before and after it by a straight line of green tiles
# the list wraps, so the first red tile is also connected to the last red tile
# tiles that are adjacent in your list will always be either on the same row or the same column


def print_grid(vertices, edges):
    xs = [v[0] for v in vertices]
    ys = [v[1] for v in vertices]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = [["." for _ in range(width)] for _ in range(height)]

    for start, end in edges:
        x1, y1 = start
        x2, y2 = end

        if x1 == x2:  # Vertical
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y - min_y][x1 - min_x] = "G"
        else:  # Horizontal
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1 - min_y][x - min_x] = "G"

    for x, y in vertices:
        grid[y - min_y][x - min_x] = "R"

    for row in grid:
        print("".join(row))


def part_two(input_file):
    vertices = read_input(input_file)
    n = len(vertices)
    edges = []
    for i in range(n):
        edges.append((vertices[i], vertices[(i + 1) % n]))

    # print_grid(vertices, edges)

    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            c1 = vertices[i]
            c2 = vertices[j]

            area = get_area(c1, c2)

            if area <= max_area:
                continue

            if is_valid_rectangle(c1, c2, edges):
                max_area = area

    return max_area


if __name__ == "__main__":
    print("Sample:", part_one("2025/09/sample-input.txt"))
    print("Real:", part_one("2025/09/input.txt"))
    print("Sample Part 2:", part_two("2025/09/sample-input.txt"))
    print("Real Part 2:", part_two("2025/09/input.txt"))  # 1613305596
