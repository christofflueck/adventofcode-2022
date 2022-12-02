from run_util import run_puzzle

scores = dict()
scores[('A', 'X')] = 3
scores[('B', 'Y')] = 3
scores[('C', 'Z')] = 3

scores[('A', 'Y')] = 6
scores[('B', 'Z')] = 6
scores[('C', 'X')] = 6

scores[('A', 'Z')] = 0
scores[('B', 'X')] = 0
scores[('C', 'Y')] = 0

outcomes = dict()
# Loose
outcomes[('A', 'X')] = 'Z'
outcomes[('B', 'X')] = 'X'
outcomes[('C', 'X')] = 'Y'

# Draw
outcomes[('A', 'Y')] = 'X'
outcomes[('B', 'Y')] = 'Y'
outcomes[('C', 'Y')] = 'Z'

# Win
outcomes[('A', 'Z')] = 'Y'
outcomes[('B', 'Z')] = 'Z'
outcomes[('C', 'Z')] = 'X'

def get_score(a, b):
    total = 0
    match b:
        case 'X': total += 1
        case 'Y': total += 2
        case 'Z': total += 3
    total += scores[(a, b)]
    return total


def part_a(data):
    input = [[str(s) for s in games.split(' ')] for games in data.split('\n')]

    return sum([get_score(s[0], s[1]) for s in input])


def part_b(data):
    input = [[str(s) for s in games.split(' ')] for games in data.split('\n')]

    total = 0
    for [opponent, outcome] in input:
        my_play = outcomes[(opponent, outcome)]
        result = get_score(opponent, my_play)
        total += result

    return total


def main():
    examples = [
        ("""A Y
B X
C Z""", 15, 12)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
