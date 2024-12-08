import numpy as np


def part1():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()

    for index, line in enumerate(data):
        data[index] = list(line)

    nodes = {}

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] not in nodes and data[y][x] != ".":
                nodes[data[y][x]] = [[x, y]]
            elif data[y][x] != ".":
                nodes[data[y][x]].append([x, y])

    def is_valid(x1, y1, x2, y2):
        p1 = np.matrix([x1, y1])
        p2 = np.matrix([x2, y2])

        direction_vector = p2 - p1

        a1 = p1 - direction_vector
        a2 = p1 + (2 * direction_vector)

        a1 = np.array(a1).flatten()
        a2 = np.array(a2).flatten()

        def in_bounds(x, y):
            if x < 0 or y < 0:
                return False
            elif x >= len(data[0]) or y >= len(data):
                return False
            return True

        valid_anti_nodes = []
        if in_bounds(a1[0], a1[1]):
            valid_anti_nodes.append([a1[0], a1[1]])
        if in_bounds(a2[0], a2[1]):
            valid_anti_nodes.append([a2[0], a2[1]])

        return valid_anti_nodes


    valid_nodes = []
    for key, coordinates in nodes.items():
        for index, value in enumerate(coordinates):
            if index == len(coordinates) - 1:
                pass
            else:
                for i in range(index + 1, len(coordinates)):
                    results = is_valid(value[0], value[1], coordinates[i][0], coordinates[i][1])
                    for result in results:
                        valid_nodes.append(result)


    unique_nodes = []
    for item in valid_nodes:
        if item not in unique_nodes:
            unique_nodes.append(item)
    print(len(unique_nodes))


def part2():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()

    for index, line in enumerate(data):
        data[index] = list(line)

    nodes = {}

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] not in nodes and data[y][x] != ".":
                nodes[data[y][x]] = [[x, y]]
            elif data[y][x] != ".":
                nodes[data[y][x]].append([x, y])

    def calc_anti_nodes(x1, y1, x2, y2):
        def is_co_linear(x1, y1, x2, y2, x, y):
            array = np.matrix([[x1, y1, 1],
                               [x2, y2, 1],
                               [x, y, 1]])

            return abs(np.linalg.det(array)) < 1e-9

        """
        y - y1 - mx + mx1 = 0
        m = (y2 - y1) / (x2 - x1)
        """

        m = (y2 - y1) / (x2 - x1)

        valid_points = []
        for x in range(len(data[0])):
            for y in range(len(data)):
                if y - y1 - m * (x - x1) == 0:
                    valid_points.append([x, y])


        valid_anti_nodes = []
        for point in valid_points:
            if is_co_linear(x1, y1, x2, y2, point[0], point[1]):
                valid_anti_nodes.append(point)

        return valid_anti_nodes

    valid_nodes = []
    for key, coordinates in nodes.items():
        for index, value in enumerate(coordinates):
            if index == len(coordinates) - 1:
                pass
            else:
                for i in range(index + 1, len(coordinates)):
                    results = calc_anti_nodes(value[0], value[1], coordinates[i][0], coordinates[i][1])
                    for result in results:
                        if result not in valid_nodes:
                            valid_nodes.append(result)

    print(len(valid_nodes))


part2()
