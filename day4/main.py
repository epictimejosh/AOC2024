import re


def part1():
    with open("data.txt", 'r') as file:
        data = file.readlines()

    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (1, 1),  # Down-Right
        (-1, -1),  # Up-Left
        (1, -1),  # Down-Left
        (-1, 1)  # Up-Right
    ]

    word = "XMAS"
    word_len = 4
    total = 0

    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == word[0]:  # Look for 'X'
                for dr, dc in directions:
                    try:
                        if all(
                                0 <= row + i * dr < len(data) and
                                0 <= col + i * dc < len(line) and
                                data[row + i * dr][col + i * dc] == word[i]
                                for i in range(word_len)
                        ):
                            total += 1
                    except IndexError:
                        pass

    print(total)


def part2():
    with open("data.txt", 'r') as file:
        data = file.readlines()

    for index, line in enumerate(data):
        data[index] = list(line)

    A_poses = []
    for col in range(1, 139):
        for row in range(1, 139):
            if data[row][col] == "A":
                A_poses.append((col, row))


    total = 0

    for element in A_poses:
        x, y = element[0], element[1]

        if data[y - 1][x - 1] == "M" and data[y + 1][x + 1] == "S":
            if data[y - 1][x + 1] == "M" and data[y + 1][x - 1] == "S" or \
                    data[y - 1][x + 1] == "S" and data[y + 1][x - 1] == "M":
                total += 1

        elif data[y - 1][x - 1] == "S" and data[y + 1][x + 1] == "M":
            if data[y - 1][x + 1] == "M" and data[y + 1][x - 1] == "S" or \
                    data[y - 1][x + 1] == "S" and data[y + 1][x - 1] == "M":
                total += 1

    print(total)


part2()