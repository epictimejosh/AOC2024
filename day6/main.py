import copy


def part1():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()

    directions = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }

    direction_order = ["up", "right", "down", "left"]

    def find_guard():
        for y, elem in enumerate(data):
            if "^" in elem:
                for x in range(len(elem)):
                    if "^" == elem[x]:
                        return x, y

    def find_coords(x, y):
        if 0 <= y < len(data) and 0 <= x < len(data[y]):
            return data[y][x]
        return None

    def find_next_pos(pos, direction):
        dx, dy = directions[direction]
        new_pos = (pos[0] + dx, pos[1] + dy)

        if find_coords(*new_pos) == ".":
            return new_pos, direction
        elif find_coords(*new_pos) == "#":
            new_direction = direction_order[
                (direction_order.index(direction) + 1) % len(direction_order)
            ]
            return find_next_pos(pos, new_direction)

        return (-1, -1), None


    pos = find_guard()
    direction = "up"
    unique_coords = []
    while pos != (-1, -1):
        pos, direction = find_next_pos(pos, direction)
        if pos not in unique_coords:
            unique_coords.append(pos)

    print(len(unique_coords))


def part2():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()

    directions = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }

    direction_order = ["up", "right", "down", "left"]

    def find_guard():
        for y, elem in enumerate(data):
            if "^" in elem:
                for x in range(len(elem)):
                    if "^" == elem[x]:
                        return x, y

    def find_coords(x, y):
        if 0 <= y < len(data) and 0 <= x < len(data[y]):
            return data[y][x]
        return None

    def find_next_pos(pos, direction):
        dx, dy = directions[direction]
        new_pos = (pos[0] + dx, pos[1] + dy)

        if find_coords(*new_pos) == ".":
            return new_pos, direction
        elif find_coords(*new_pos) == "#":
            new_direction = direction_order[
                (direction_order.index(direction) + 1) % len(direction_order)
            ]
            return find_next_pos(pos, new_direction)

        return (-1, -1), None


    total = 0
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if find_coords(x, y) == "#" or find_coords(x, y) == "^":
                pass
            else:
                print((x+(y*len(data[0]))),"/",str(len(data)*len(data[0])))
                print(total)
                data_copy = copy.deepcopy(data)
                new_string = data_copy[y][:x] + "#" + data_copy[y][x + 1:]
                data_copy[y] = new_string
                pos = find_guard()
                direction = "up"
                unique_coords = []
                while pos != (-1, -1):
                    pos, direction = find_next_pos(pos, direction)
                    if (pos, direction) not in unique_coords:
                        unique_coords.append((pos, direction))
                    elif (pos, direction) in unique_coords:
                        total += 1
                        pos = (-1, -1)

    print(total)

part2()
