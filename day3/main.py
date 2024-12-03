import re


def part1():
    with open("data.txt", "r") as f:
        file_data = f.read().splitlines()

    file_data = "".join(file_data)

    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

    results = re.findall(pattern, file_data)

    sum = 0

    for elem in results:
        result = elem[4:len(elem)-1].split(",")
        value1, value2 = int(result[0]), int(result[1])

        sum += (value1 * value2)

    print(sum)


def part2():
    with open("data.txt", "r") as f:
        file_data = f.read().splitlines()

    file_data = "".join(file_data)

    pattern = r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(don't\(\))|(do\(\))"

    results = re.findall(pattern, file_data)

    elements = []
    for elem in results:
        if elem[0] != "":
            elements.append(elem[0])
        elif elem[1] != "":
            elements.append(elem[1])
        else:
            elements.append(elem[2])

    allowed = True
    sum = 0
    for elem in elements:
        if elem == "don't()":
            allowed = False
        elif elem == "do()":
            allowed = True
        else:
            if allowed:
                data = elem[4:len(elem)-1].split(",")
                value1, value2 = int(data[0]), int(data[1])
                sum += (value1 * value2)

    print(sum)

part2()
