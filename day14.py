from run_util import run_puzzle

DIRS = [(0, 1), (-1, 1), (1, 1)]


def get_next_pos(cave, sand):
    for dir_x, dir_y in DIRS:
        next_pos = (dir_x + sand[0], dir_y + sand[1])
        if next_pos not in cave:
            return next_pos
    return None


def part_a(data):
    cave, floor = parse_data(data)

    sand_start = (500, 0)
    curr_sand = (500, 0)

    while curr_sand[1] < floor:
        next_pos = get_next_pos(cave, curr_sand)
        if next_pos is not None:
            curr_sand = next_pos
        else:
            cave[curr_sand] = -1
            curr_sand = sand_start

    return abs(sum(x for x in cave.values() if x == -1))


def parse_data(data):
    paths = []
    floor = 0
    for strpath in data.split('\n'):
        path = []
        for coords in strpath.split():
            if coords != '->':
                x, y = coords.split(',')
                path.append((int(x), int(y)))
                floor = max(int(y), floor)
        paths.append(path)
    cave = {}
    for path in paths:
        for i in range(1, len(path)):
            start_x, start_y = path[i - 1]
            stop_x, stop_y = path[i]
            if start_x == stop_x:
                for y in range(min(start_y, stop_y), max(start_y, stop_y) + 1):
                    cave[(start_x, y)] = 1
            else:
                for x in range(min(start_x, stop_x), max(start_x, stop_x) + 1):
                    cave[(x, start_y)] = 1
    return cave, floor


def print_cave(cave, curr_sand=(0, 0)):
    print('--------------------------')
    for y in range(0, 12):
        row = ''
        for x in range(493, 504):
            if x == curr_sand[0] and y == curr_sand[1]:
                row += 'x'
            elif (x, y) in cave:
                if cave[x, y] == 1:
                    row += '#'
                else:
                    row += 'o'
            else:
                row += '.'
        print(row)


def get_next_pos_floor(cave, sand, floor):
    for dir_x, dir_y in DIRS:
        next_pos = (dir_x + sand[0], dir_y + sand[1])
        if next_pos not in cave and next_pos[1] < floor:
            return next_pos
    return None


def part_b(data):
    cave, floor = parse_data(data)

    floor += 2

    sand_start = (500, 0)
    curr_sand = (500, 0)

    while sand_start not in cave:
        next_pos = get_next_pos_floor(cave, curr_sand, floor)
        if next_pos is not None:
            curr_sand = next_pos
        else:
            cave[curr_sand] = -1
            curr_sand = sand_start

    return abs(sum(x for x in cave.values() if x == -1))


def main():
    examples = [
        ("""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""", 24, 93)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
