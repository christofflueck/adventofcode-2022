import functools
import json
from run_util import run_puzzle


def parse_data(data):
    return [[json.loads(packet) for packet in pair.split('\n')] for pair in data.split('\n\n')]


def compare(left, right):
    len_left = len(left)
    len_right = len(right)
    for i in range(min(len_right, len_left)):
        val_left = left[i]
        val_right = right[i]

        type_left = type(val_left)
        type_right = type(val_right)
        if type_left is int and type_right is int:
            if val_left < val_right:
                return -1
            if val_left > val_right:
                return 1
            continue

        if type_left is list and type_right is int:
            val_right = [val_right]

        if type_left is int and type_right is list:
            val_left = [val_left]

        result = compare(val_left, val_right)
        if result != 0:
            return result
    if len_left < len_right:
        return -1
    if len_right < len_left:
        return 1

    return 0


def part_a(data):
    pairs = parse_data(data)

    in_order = []

    for pair_index, [left, right] in enumerate(pairs):
        if compare(left, right) == -1:
            in_order.append(pair_index + 1)

    return sum(in_order)


def part_b(data):
    packets = [packet for pair in parse_data(data) for packet in pair]
    dividers = [[2]], [[6]]
    packets += dividers

    packets.sort(key=functools.cmp_to_key(compare))

    return (packets.index(dividers[0]) + 1) * (packets.index(dividers[1]) + 1)


def main():
    examples = [
        ("""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""", 13, 140)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
