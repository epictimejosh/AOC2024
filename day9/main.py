

def part1():
    with open ("data.txt", "r") as f:
        data = f.read().strip()

    disk = []
    current_file_id = 0

    for index, element in enumerate(data):
        if index % 2 == 0:
            disk.extend([current_file_id] * int(element))
            current_file_id += 1
        else:
            disk.extend(["."] * int(element))

    for i in range(len(disk) - 1, -1, -1):
        if disk[i] != ".":
            for j in range(len(disk)):
                if disk[j] == ".":
                    disk[j] = disk[i]
                    disk[i] = "."
                    break

    total = 0
    for index, value in enumerate(disk[1:]):
        if value != ".":
            total += index * int(value)

    print(total)


def part2():
    with open("data.txt", "r") as f:
        data = f.read().strip()


    disk = []
    current_file_id = 0
    for index, element in enumerate(data):
        length = int(element)
        if index % 2 == 0:
            if length > 0:
                disk.extend([current_file_id] * length)
                current_file_id += 1
        else:
            if length > 0:
                disk.extend(["."] * length)


    total_files = current_file_id

    def find_file_run(disk, file_id):
        try:
            start = disk.index(file_id)
        except ValueError:
            return None, 0
        length = 0
        pos = start
        while pos < len(disk) and disk[pos] == file_id:
            length += 1
            pos += 1
        return start, length


    def find_free_space(disk, file_length, file_start):
        free_count = 0
        run_start = None
        best_start = None

        for i in range(file_start):
            if disk[i] == ".":
                if run_start is None:
                    run_start = i
                free_count += 1
            else:
                if free_count >= file_length:
                    best_start = run_start
                    break
                free_count = 0
                run_start = None

        if run_start is not None and free_count >= file_length and best_start is None:
            best_start = run_start

        return best_start


    for file_id in range(total_files - 1, -1, -1):
        start, length = find_file_run(disk, file_id)
        if length == 0:
            continue

        target_start = find_free_space(disk, length, start)
        if target_start is not None:

            for i in range(start, start + length):
                disk[i] = "."

            for i in range(target_start, target_start + length):
                disk[i] = file_id


    total = 0
    for index, value in enumerate(disk):
        if value != ".":
            total += index * int(value)

    print(total)


part2()
