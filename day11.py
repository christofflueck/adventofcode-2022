from typing import Tuple

from run_util import run_puzzle
from parse import *
import math

class Monkey:

    def __init__(self, input: str) -> None:
        super().__init__()
        lines = input.split('\n')
        self.num = parse("Monkey {:d}:", lines[0])[0]
        self.items = [d[0] for d in findall("{:d}", lines[1])]
        op, value = search("  Operation: new = old {} {:w}", lines[2])

        match (op, value):
            case ('*', 'old'):
                self.operation = lambda x: x * x
            case ('*', value):
                self.operation = (lambda value: lambda x: x * value)(int(value))
            case ('+', value):
                self.operation = (lambda value: lambda x: x + value)(int(value))

        self.divisor, = search("{:d}", lines[3])
        self.true_target, = search("{:d}", lines[4])
        self.false_target, = search("{:d}", lines[5])
        self.items_inspected = 0
        self.inspect = lambda x: x // 3

    def __str__(self) -> str:
        return "Monkey {}: {}".format(self.num, ', '.join([str(i) for i in self.items]))

    def inspect_item(self) -> Tuple[int, int]:
        self.items_inspected += 1
        item = self.items.pop(0)

        new = self.operation(item)
        new = self.inspect(new)

        if new % self.divisor == 0:
            return self.true_target, new
        else:
            return self.false_target, new


def part_a(data):
    monkeys = [Monkey(inp) for inp in data.split('\n\n')]

    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                target, item = monkey.inspect_item()
                monkeys[target].items.append(item)

    return math.prod(sorted([monkey.items_inspected for monkey in monkeys])[-2:])


def part_b(data):
    monkeys = [Monkey(inp) for inp in data.split('\n\n')]
    product = math.prod([monkey.divisor for monkey in monkeys])
    for monkey in monkeys:
        monkey.inspect = lambda x = product: x % product

    for _ in range(10000):
        for monkey in monkeys:
            while monkey.items:
                target, item = monkey.inspect_item()
                monkeys[target].items.append(item)

    return math.prod(sorted([monkey.items_inspected for monkey in monkeys])[-2:])


def main():
    examples = [
        ("""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""", 10605, 2713310158)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
