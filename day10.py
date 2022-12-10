from run_util import run_puzzle
from advent_of_code_ocr import convert_6


def part_a(data):
    commands = data.split('\n')

    cycle = 0
    strengths = []
    x = 1

    for command in commands:
        cycle = inc_cycle(cycle, strengths, x)

        match command.split():
            case ["noop"]: pass
            case ["addx", num]:
                cycle = inc_cycle(cycle, strengths, x)
                x += int(num)
            case other: print("unknown command found", other)

    return sum(s[0] * s[1] for s in strengths)


def inc_cycle(cycle, strengths, x):
    cycle += 1
    if cycle % 40 == 20:
        strengths.append((cycle, x))
    return cycle


def inc_cycle_2(cycle, x, screen):
    cycle += 1
    screen[cycle - 1] = '#' if abs(x - ((cycle - 1) % 40)) <= 1 else '.'
    return cycle


def part_b(data):
    commands = data.split('\n')

    cycle = 0
    x = 1

    screen = ['' for _ in range(241)]

    for command in commands:
        cycle = inc_cycle_2(cycle, x, screen)

        match command.split():
            case ["noop"]: pass
            case ["addx", num]:
                cycle = inc_cycle_2(cycle, x, screen)
                x += int(num)
            case other: print("unknown command found", other)

    s = []
    for i in range(cycle // 40):
        s.append(''.join(screen[i*40:(i*40)+40]))

    return convert_6('\n'.join(s))


def main():
    examples = [
        ("""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""", 13140, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
