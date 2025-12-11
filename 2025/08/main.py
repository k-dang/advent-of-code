# figure out which junction boxes to connect, so that electricity can reach every junction box

# one junction box per line
# each postion is given as x,y,z coordinates

# the elves would like to focus on connecting pairs of junction boxes
# that are as close together as possible according to straight-line distance (euclidean distance)1

# when 2 junction boxes are connected, they become part of the same curcuit
# single circuit between 2 junction boxes

# next closest could be added to the circuit as well or form a new circuit

# multiple together the 3 largest circuits


def read_input(file_name):
    with open(file_name, "r") as f:
        return [tuple(line.strip().split(",")) for line in f]


def euclidean_distance(junction_box_1, junction_box_2):
    return (
        (int(junction_box_1[0]) - int(junction_box_2[0])) ** 2
        + (int(junction_box_1[1]) - int(junction_box_2[1])) ** 2
        + (int(junction_box_1[2]) - int(junction_box_2[2])) ** 2
    ) ** 0.5


class UnionFind:
    def __init__(self, elements):
        self.parent = {e: e for e in elements}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY


def part_one(file_name, limit):
    data = read_input(file_name)

    distances = []
    # iterate over the list and find 2 entries that are closest to each other
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            distance = euclidean_distance(data[i], data[j])
            distances.append((distance, data[i], data[j]))

    distances.sort(key=lambda x: x[0])

    uf = UnionFind(data)

    # connect the top limit pairs
    for k in range(min(limit, len(distances))):
        _, junction_box_1, junction_box_2 = distances[k]
        uf.union(junction_box_1, junction_box_2)

    # calculate circuit sizes
    circuit_sizes = {}
    for box in data:
        root = uf.find(box)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

    sizes = sorted(circuit_sizes.values(), reverse=True)
    print(f"Top sizes: {sizes[:5]}")

    return sizes[0] * sizes[1] * sizes[2]


# we need to connect closest pairs until all are connected
# then multiple the X coords of the last 2 boxes in the circuit
def part_two(file_name):
    data = read_input(file_name)

    distances = []
    # iterate over the list and find 2 entries that are closest to each other
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            distance = euclidean_distance(data[i], data[j])
            distances.append((distance, data[i], data[j]))

    distances.sort(key=lambda x: x[0])

    uf = UnionFind(data)
    num_components = len(data)

    # connect all the pairs
    for distance, box_1, box_2 in distances:
        if uf.find(box_1) != uf.find(box_2):
            uf.union(box_1, box_2)
            num_components -= 1
            if num_components == 1:
                # These are the last two boxes connected that made the circuit complete
                return int(box_1[0]) * int(box_2[0])

    return 0


if __name__ == "__main__":
    print("Sample:", part_one("2025/08/sample-input.txt", 10))
    print("Real:", part_one("2025/08/input.txt", 1000))

    print("Sample:", part_two("2025/08/sample-input.txt"))
    print("Real:", part_two("2025/08/input.txt"))
