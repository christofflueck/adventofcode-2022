from run_util import run_puzzle


def part_a(data: str):
    for i in range(4, len(data)):
        marker = data[i - 4:i]
        if len(set(marker)) == len(marker):
            return i
    return 0


def part_b(data):
    for i in range(14, len(data)):
        marker = data[i - 14:i]
        if len(set(marker)) == len(marker):
            return i
    return 0


def main():
    examples = [
        ("""mjqjpqmgbljsphdztnvjfqwrcgsmlb""", 7, 19),
        ("""bvwbjplbgvbhsrlpgdmjqwftvncz""", 5, 23),
        ("""nppdvjthqldpwncqszvftbrmjlhg""", 6, 23),
        ("""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg""", 10, 29),
        ("""zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw""", 11, 26),
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
