def test_array(report):
    increase = True

    sorted_array = sorted(report)
    if report == sorted_array or report == sorted_array[::-1]:
        for index in range(len(report) - 1):
            value = report[index] - report[index + 1]
            if value < 0:
                value = value * -1
            if not (value >= 1 and value <= 3):
                increase = False
                break
    else:
        increase = False

    return increase


def part1():
    with open("data.txt", "r") as f:
        file_data = f.read().splitlines()

    data = [list(map(int, elem.split())) for elem in file_data]

    num_safe = 0
    for report in data:
        if test_array(report):
            num_safe += 1
    print(num_safe)


def part2():
    with open("data.txt", "r") as f:
        file_data = f.read().splitlines()

    data = [list(map(int, elem.split())) for elem in file_data]

    num_safe = 0
    for report in data:
        increase = False
        for index in range(len(report)):
            temp_array = report.copy()
            del temp_array[index]

            if test_array(temp_array):
                increase = True
                break


        if increase:
            num_safe += 1

    print(num_safe)


part2()