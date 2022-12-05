from run_util import run_puzzle
from parse import *
import re


def parse_input(data):
    moves = []
    stacks = {}
    for line in reversed(data.split('\n')):
        if 'move' in line:
            moves.append(parse("move {:d} from {:d} to {:d}", line))
        elif line == '':
            continue
        else:
            m = re.findall('( \d+ )+', line)
            if m:
                for group in m:
                    stacks[int(group)] = []
            else:
                for key in stacks.keys():
                    value = line[(key - 1) * 4 + 1]
                    if value != ' ':
                        stacks[key].append(value)
    return moves, stacks


def part_a(data):
    moves, stacks = parse_input(data)

    while moves:
        num, src, trg = moves.pop()
        for _ in range(num):
            stacks[trg].append(stacks[src].pop())

    return ''.join([stack[-1] for stack in stacks.values()])


def part_b(data):
    moves, stacks = parse_input(data)
    while moves:
        num, src, trg = moves.pop()
        to_move = stacks[src][-num:]
        stacks[src] = stacks[src][:-num]
        stacks[trg].extend(to_move)
    return ''.join([stack[-1] for stack in stacks.values()])


def main():
    examples = [
        ("""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""", "CMZ", "MCD")
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
