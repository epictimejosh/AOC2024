
def part1():
    with open("data.txt", "r") as f:
        file_contents = f.read().splitlines()

    left = [int(line[:5]) for line in file_contents]
    right = [int(line[8:]) for line in file_contents]

    # Sort left and right lists
    left.sort()
    right.sort()

    total_sum = 0
    for l, r in zip(left, right):
        value = abs(l - r)
        total_sum += value

    print(total_sum)


def part2():
    with open("data.txt", "r") as f:
        file_contents = f.read().splitlines()

    left = [int(line[:5]) for line in file_contents]
    right = [int(line[8:]) for line in file_contents]

    # Transform left based on occurrences in right
    for i in range(len(left)):
        check_value = left[i]
        sum_count = right.count(check_value)
        left[i] = check_value * sum_count

    total = sum(left)
    print(total)


part2()