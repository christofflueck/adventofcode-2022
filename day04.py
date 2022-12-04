from run_util import run_puzzle


def part_a(data):
    pairs = [[[int(x) for x in assignment.split('-')] for assignment in pair.split(',')] for pair in data.split('\n')]
    total = 0
    for a1, a2 in pairs:
        if (a1[0] >= a2[0] and a1[1] <= a2[1]) or (a2[0] >= a1[0] and a2[1] <= a1[1]):
            total += 1
    return total


def part_b(data):
    pairs = [[[int(x) for x in assignment.split('-')] for assignment in pair.split(',')] for pair in data.split('\n')]
    total = 0
    for a1, a2 in pairs:
        s1 = set(range(a1[0], a1[1] + 1))
        s2 = set(range(a2[0], a2[1] + 1))
        if len(s1.intersection(s2)):
            total += 1
    return total


def main():
    examples = [
        ("""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""", 2, 4)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
