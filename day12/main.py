

def part1():
    with open("data.txt", "r") as f:
        raw_data = f.read().splitlines()
    data = [list(line) for line in raw_data]

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def search_area(letter, x, y, visited, area_sum=0, perimeter_sum=0):
        if (x, y) in visited:
            return area_sum, perimeter_sum

        visited.add((x, y))

        area_sum += 1


        for direction in directions:
            temp_x = x + direction[0]
            temp_y = y + direction[1]

            if 0 <= temp_x < len(data[0]) and 0 <= temp_y < len(data):
                if data[temp_y][temp_x] == letter:
                    area_sum, perimeter_sum = search_area(letter, temp_x, temp_y, visited, area_sum, perimeter_sum)
                else:
                    if (temp_x, temp_y) not in completed:
                        perimeter_sum += 1
            else:
                if (temp_x, temp_y) not in completed:
                    perimeter_sum += 1

        return area_sum, perimeter_sum

    total = 0
    completed = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (x, y) not in completed:
                letter = char
                visited = set()
                area_sum, perimeter_sum = search_area(letter, x, y, visited)
                completed.update(visited)
                total += (area_sum * perimeter_sum)
                print(f"{letter}: {area_sum} x {perimeter_sum} = {area_sum * perimeter_sum}")

    print(total)


part1()
