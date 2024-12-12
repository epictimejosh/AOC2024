

def parr1():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()

    data = [list(map(int, d)) for d in data]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    rows = len(data)
    cols = len(data[0])

    def dfs(x, y, seen_nines, current_val):
        if data[y][x] == 9:
            seen_nines.add((x, y))
            return

        next_val = current_val + 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows:
                if data[ny][nx] == next_val:
                    dfs(nx, ny, seen_nines, next_val)

    total = 0
    for y in range(rows):
        for x in range(cols):
            if data[y][x] == 0:
                seen_nines = set()
                dfs(x, y, seen_nines, 0)
                total += len(seen_nines)

    print(total)


def part2():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()

    data = [list(map(int, d)) for d in data]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    rows = len(data)
    cols = len(data[0])

    starts = []
    for y in range(rows):
        for x in range(cols):
            if data[y][x] == 0:
                starts.append((x, y))

    def count_paths(x, y):
        current_height = data[y][x]
        if current_height == 9:
            return 1

        total_paths = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows:
                if data[ny][nx] == current_height + 1:
                    total_paths += count_paths(nx, ny)

        return total_paths

    total = 0
    for start in starts:
        total += count_paths(*start)

    print(total)


part2()
