from run_util import run_puzzle
import string


def part_a(data):
    backpacks = [(set(x[:len(x)//2]), set(x[len(x)//2:])) for x in data.split('\n')]
    return sum([sum([string.ascii_letters.index(x) + 1 for x in comp1.intersection(comp2)]) for comp1,comp2 in backpacks])


def part_b(data):
    backpacks = [set(x) for x in data.split('\n')]
    return sum(sum([string.ascii_letters.index(x) + 1 for x in set.intersection(*backpacks[i*3:i*3+3])]) for i in range(len(backpacks) // 3))


def main():
    examples = [
        ("""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""", 157, 70)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
