

def part1():
    def test_sequence(answer, sequence):
        num_slots = len(sequence) - 1
        num_configurations = 2 ** num_slots

        # Iterate over each configuration
        for config_index in range(num_configurations):
            current_value = sequence[0]
            temp_config = []

            config = config_index
            for _ in range(num_slots):
                temp_config.append(config % 2)
                config //= 2

            for i, op in enumerate(temp_config):
                if op == 0:  # Addition
                    current_value += sequence[i + 1]
                elif op == 1:  # Multiplication
                    current_value *= sequence[i + 1]

            if current_value == answer:
                return True

        return False
    with open("data.txt", "r") as f:
        data = f.read().splitlines()

    organised_data = []
    for line in data:
        line = line.split(": ")
        organised_data.append([int(line[0]), list(map(int, line[1].split(" ")))])


    total = 0
    for sequence in organised_data:
        if test_sequence(sequence[0], sequence[1]):
            total += sequence[0]

    print(total)


def part2():
    def test_sequence(answer, sequence):
        n = len(sequence)
        queue = [(1, sequence[0])]

        while queue:
            i, val = queue.pop()


            if i == n:
                if val == answer:
                    return True
                continue


            possibilities = [
                val + sequence[i],
                val * sequence[i],
                int(f'{val}{sequence[i]}')
            ]

            for p in possibilities:
                if p <= answer:
                    queue.append((i + 1, p))

        return False


    with open("data.txt", "r") as f:
        data = f.read().splitlines()

    organised_data = []
    for line in data:
        left, right = line.split(": ")
        organised_data.append([int(left), list(map(int, right.split()))])

    total = 0
    for sequence in organised_data:
        if test_sequence(sequence[0], sequence[1]):
            total += sequence[0]

    print(total)


part2()

