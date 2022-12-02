from run_util import run_puzzle


def part_a(data):
    input = [0 if x == '' else int(x) for x in data.split('\n')]
    elfs = get_elfs(input)
    return max(elfs)


def get_elfs(input):
    curr = 0
    elfs = []
    for i in input:
        if i == 0:
            elfs.append(curr)
            curr = 0
        else:
            curr += i
    if curr > 0:
        elfs.append(curr)
    return elfs


def part_b(data):
    input = [0 if x == '' else int(x) for x in data.split('\n')]
    elfs = get_elfs(input)
    top3 = 0
    for _ in range(3):
        top = max(elfs)
        top3 += top
        print(top)
        elfs.remove(top)
    return top3


def main():
    examples = [
        ("""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""", 24000, 45000)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
