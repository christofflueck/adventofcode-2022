from parse import parse

from run_util import run_puzzle


def part_a(data):
    input = [parse('Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}', x) for x in data.split('\n')]
    pairs = [((sx, sy), (bx, by)) for sx, sy, bx, by in input]

    target_row = 10 if pairs[0][0][0] == 2 else 2000000

    area = set()
    blocked = set()

    for sensor, beacon in pairs:
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacon

        distance = get_distance(beacon, sensor)
        if sensor_y == target_row:
            blocked.add(sensor)
        if beacon_y == target_row:
            blocked.add(beacon)

        target_diff_y = target_row - sensor_y
        if abs(target_diff_y) <= distance:
            max_x = distance - abs(target_diff_y)
            for x in range(-max_x, max_x + 1):
                area.add((sensor_x + x, target_row))

        print('pair')

    return len([x for x in area if x not in blocked])


def get_distance(beacon, sensor):
    sensor_x, sensor_y = sensor
    beacon_x, beacon_y = beacon
    diff_x = abs(sensor_x - beacon_x)
    diff_y = abs(sensor_y - beacon_y)
    distance = diff_x + diff_y
    return distance


def safe_add_possible(possible, x, y, max_coord):
    if max_coord >= x >= 0 and max_coord >= y >= 0:
        possible.add((x, y))


def part_b(data):
    input = [parse('Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}', x) for x in data.split('\n')]
    pairs = [((sx, sy), (bx, by)) for sx, sy, bx, by in input]
    max_coord = 20 if pairs[0][0][0] == 2 else 4000000

    possible = set()
    for sensor, beacon in pairs:
        distance = get_distance(beacon, sensor) + 1
        sensor_x, sensor_y = sensor

        safe_add_possible(possible, sensor_x - distance, sensor_y, max_coord)
        safe_add_possible(possible, sensor_x + distance, sensor_y, max_coord)

        possible = set([b for b in possible if get_distance(b, sensor) > distance - 1])
        for diff_x in range(-distance, distance + 1):
            safe_add_possible(possible, sensor_x + diff_x, sensor_y - (distance - abs(diff_x)), max_coord)
            safe_add_possible(possible, sensor_x + diff_x, sensor_y + (distance - abs(diff_x)), max_coord)

    for sensor, beacon in pairs:
        distance = get_distance(beacon, sensor)
        possible = set([b for b in possible if get_distance(b, sensor) > distance])

    x, y = possible.pop()
    return x * 4000000 + y


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
Sensor at x=20, y=1: closest beacon is at x=15, y=3""", 26, 56000011)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
