from run_util import run_puzzle

DIRS = {
    'R': (0, 1),
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0)
}


def part_a(data):
    steps = parse_steps(data)

    tail_history = set()
    tail = [0, 0]
    head = [0, 0]

    for direction, amount in steps:
        for _ in range(amount):
            head[0] += DIRS[direction][0]
            head[1] += DIRS[direction][1]

            diff_x = head[1] - tail[1]
            diff_y = head[0] - tail[0]

            if abs(diff_y) > 1 or abs(diff_x) > 1:
                if head[0] == tail[0]:
                    tail[1] += diff_x / abs(diff_x)
                elif head[1] == tail[1]:
                    tail[0] += diff_y / abs(diff_y)
                else:
                    tail[1] += diff_x / abs(diff_x)
                    tail[0] += diff_y / abs(diff_y)

            tail_history.add(tuple(tail))

    return len(tail_history)


def parse_steps(data):
    steps = []
    for row in data.split('\n'):
        direction, amount = row.split()
        steps.append((direction, int(amount)))
    return steps


def part_b(data):
    steps = parse_steps(data)

    tail_history = set()
    rope = [[0, 0] for _ in range(10)]

    for direction, amount in steps:
        for _ in range(amount):
            rope[0][0] += DIRS[direction][0]
            rope[0][1] += DIRS[direction][1]

            for i in range(len(rope) - 1):
                head = rope[i]
                tail = rope[i + 1]

                diff_x = head[1] - tail[1]
                diff_y = head[0] - tail[0]

                if abs(diff_y) > 1 or abs(diff_x) > 1:
                    if head[0] == tail[0]:
                        tail[1] += diff_x / abs(diff_x)
                    elif head[1] == tail[1]:
                        tail[0] += diff_y / abs(diff_y)
                    else:
                        tail[1] += diff_x / abs(diff_x)
                        tail[0] += diff_y / abs(diff_y)

            tail_history.add(tuple(rope[-1]))

    return len(tail_history)


def main():
    examples = [
        ("""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""", 13, 1)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
