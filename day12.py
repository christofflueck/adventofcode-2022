from collections import deque

from run_util import run_puzzle

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(map, history, curr):
    history.append(curr)
    curr_char = map[curr]
    print(history)
    if curr_char == 'E':
        return history
    for possible_direction in DIRS:
        next_x = curr[0] - possible_direction[0]
        next_y = curr[1] - possible_direction[1]
        next_pos = (next_x, next_y)
        if next_pos in map and next_pos not in history:
            next_char = map[next_pos]
            if next_char == 'E':
                return dfs(map, history, next_pos)
            elif curr_char == 'S' or ord(next_char) <= ord(curr_char) + 1:
                next_history = dfs(map, list(history), next_pos)
                if next_history:
                    return next_history
    return None


def part_a(data):
    input = [list(x) for x in data.split('\n')]
    map = {}

    start = None
    for y in range(len(input)):
        for x in range(len(input[0])):
            map[(x, y)] = input[y][x]
            if input[y][x] == 'S':
                start = (x, y)

    result = get_path(map, start)

    return result


def get_path(map, start):
    queue = deque()
    history = set()
    history.add(start)
    queue.append(start)
    paths = {start: 0}
    result = None
    while len(queue):
        curr = queue.popleft()
        curr_char = map[curr]
        history.add(curr)
        if curr_char == 'E':
            result = paths[curr]
            break

        for possible_direction in DIRS:
            next_x = curr[0] - possible_direction[0]
            next_y = curr[1] - possible_direction[1]
            next_pos = (next_x, next_y)
            if next_pos in map and next_pos not in history and next_pos not in queue:
                next_char = map[next_pos]
                if next_char == 'E':
                    next_char = 'z'
                if curr_char == 'S' or ord(next_char) <= ord(curr_char) + 1:
                    paths[next_pos] = paths[curr] + 1
                    queue.append(next_pos)
    if result:
        return result
    return 999999


def part_b(data):
    input = [list(x) for x in data.split('\n')]
    map = {}

    starts = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            map[(x, y)] = input[y][x]
            if input[y][x] == 'S' or input[y][x] == 'a':
                starts.append((x, y))

    results = [get_path(map, start) for start in starts]

    return min(results)


def main():
    examples = [
        ("""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""", 31, 29)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
