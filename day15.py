from parse import parse

from run_util import run_puzzle


def part_a(data):
    input = [parse('Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}', x) for x in data.split('\n')]
    pairs = [((sx, sy), (bx, by)) for sx, sy, bx, by in input]

    target_row = 10 if pairs[0][0][0] == 2 else 2000000

    area = {}

    for sensor, beacon in pairs:
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacon

        diff_x = abs(sensor_x - beacon_x)
        diff_y = abs(sensor_y - beacon_y)

        distance = diff_x + diff_y
        area[sensor] = 0
        area[beacon] = 0
        for distance_y in range(-distance, distance + 1):
            remaining_distance = distance - abs(distance_y)
            for distance_x in range(-remaining_distance, remaining_distance + 1):
                point_x = sensor_x + distance_x
                point_y = sensor_y + distance_y
                point = (point_x, point_y)
                if point not in area:
                    area[point] = 1

    return sum([area[p] for p in area.keys() if p[1] == target_row])


def part_b(data):
    input = [int(x) for x in data.split(',')]
    return 0


def main():
    examples = [
        ("""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""", 26, 1)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
