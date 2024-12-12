

def part1():
    with open("data.txt", "r") as f:
        data = f.read().split()

    pages = data[:1176]
    updates = data[1177:]

    rules = []

    for rule in pages:
        parts = rule.split("|")
        x = int(parts[0])
        y = int(parts[1])
        rules.append((x, y))

    parsed_updates = []

    for update in updates:
        parts = update.split(",")
        integers = list(map(int, parts))
        parsed_updates.append(integers)

    updates = parsed_updates

    valid_updates = []

    for update in updates:
        is_valid = True
        for x, y in rules:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    is_valid = False
                    break
        if is_valid:
            valid_updates.append(update)

    total = 0
    for valid_update in valid_updates:
        total += (valid_update[len(valid_update) // 2])

    print(total)


def part2():
    data = open("data.txt ").read().split("\n\n")

    rules = {}
    for rule in data[0].split("\n"):
        a, b = rule.split("|")
        if a in rules:
            rules[a].append(b)
        else:
            rules[a] = [b]

    total = 0
    for order in data[1].split("\n"):
        tries = 0
        valid = False
        nums = order.split(",")
        while not valid:
            tries += 1
            valid = True
            new_nums = []
            for index, num in enumerate(nums[1:]):
                if num in rules and nums[index] in rules[num] and valid:
                    valid = False
                    list_parts = [nums[0:index], nums[index + 1], nums[index], nums[index + 2:]]
                    for part in list_parts:
                        if type(part) == str:
                            new_nums.append(part)
                        else:
                            for x in part:
                                new_nums.append(x)
            if not valid:
                nums = new_nums

        if tries > 1:
            total += int(nums[len(nums) // 2])

    print(total)


part2()
