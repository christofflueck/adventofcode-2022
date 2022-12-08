from run_util import run_puzzle


def part_a(data):
    trees = [[int(tree) for tree in row] for row in data.split('\n')]
    visible = [[0 for _ in row] for row in trees]

    for row_num, row in enumerate(trees):
        for col_num, tree in enumerate(row):
            if visible[row_num][col_num] > 0:
                continue
            if row_num == 0 or row_num == len(trees) - 1 or col_num == 0 or col_num == len(row) - 1:
                visible[row_num][col_num] = 1
                continue
            if max(row[:col_num]) < tree or max(row[col_num + 1:]) < tree:
                visible[row_num][col_num] = 1
                continue
            if max([colRow[col_num] for colRow in trees[:row_num]]) < tree or max(
                    [colRow[col_num] for colRow in trees[row_num + 1:]]) < tree:
                visible[row_num][col_num] = 1
                continue

    return sum([sum(row) for row in visible])


def part_b(data):
    trees = [[int(tree) for tree in row] for row in data.split('\n')]
    max_score = 0

    for row_num, row in enumerate(trees):
        for col_num, tree in enumerate(row):
            left = list(reversed(row[:col_num]))
            right = row[col_num + 1:]
            top = list(reversed([colRow[col_num] for colRow in trees[:row_num]]))
            bottom = [colRow[col_num] for colRow in trees[row_num + 1:]]

            score = 1
            for dir in [top, left, bottom, right]:
                dir_score = 0
                for dir_tree in dir:
                    dir_score += 1
                    if dir_tree >= tree:
                        break

                score *= dir_score
            max_score = max(score, max_score)

    return max_score


def main():
    examples = [
        ("""30373
25512
65332
33549
35390""", 21, 8)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
