import math


def part1():
    with open("data.txt", "r") as f:
        data = f.read()

    data = list(map(int, data.split(" ")))

    def config_number(value):
        if value == 0:
            return [1]
        elif (len(str(value)) % 2) == 0:
            value_str = str(value)
            length = len(value_str)

            first_half = int(value_str[:length // 2])
            second_half = int(value_str[length // 2:])
            return [first_half, second_half]
        else:
            return [value*2024]

    for iteration in range(75):
        print(f"{iteration + 1}/75")
        copy_list = data.copy()
        for index, element in enumerate(data):
            new_element = config_number(element)
            copy_list[index] = new_element
        data = []
        for elem in copy_list:
            for sub_elem in elem:
                data.append(sub_elem)

    print(len(data))


part1()
