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
    unique_coords = set()
    while pos != (-1, -1):
        pos, direction = find_next_pos(pos, direction)
        if pos not in unique_coords:
            unique_coords.add(pos)

    return unique_coords


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

    def find_guard(data):
        for y, elem in enumerate(data):
            if "^" in elem:
                for x in range(len(elem)):
                    if "^" == elem[x]:
                        return x, y

    def move_guard(data, start_x, start_y, obstruction=None):
        matrix = [list(row) for row in data]
        if obstruction:
            matrix[obstruction[1]][obstruction[0]] = "#"

        x, y = start_x, start_y
        direction_index = 0
        visited_positions = set()

        while True:
            if (x, y, direction_index) in visited_positions:
                return True
            visited_positions.add((x, y, direction_index))

            dx, dy = directions[direction_order[direction_index]]
            nx, ny = x + dx, y + dy

            if (
                0 <= ny < len(matrix) and
                0 <= nx < len(matrix[0]) and
                matrix[ny][nx] == "."
            ):
                x, y = nx, ny
            else:
                direction_index = (direction_index + 1) % 4

            if not (0 <= ny < len(matrix) and 0 <= nx < len(matrix[0])):
                break

        return False

    guard_x, guard_y = find_guard(data)
    loop_count = 1

    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "#" or (x, y) == (guard_x, guard_y):
                continue

            if move_guard(data, guard_x, guard_y, obstruction=(x, y)):
                loop_count += 1

    print(loop_count)


part2()
