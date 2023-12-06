import re


def solve(info: list[str]) -> int:

    def calculate_ways_to_win(stats: list[int]) -> tuple:
        time, record_distance = stats
        p1, p2 = 0, time

        p1_distance = p1 * (time - p1)
        p2_distance = p2 * (time - p2)

        while p1_distance <= record_distance and p2_distance <= record_distance:
            p1 += 1
            p2 -= 1

            p1_distance = p1 * (time - p1)
            p2_distance = p2 * (time - p2)

        return p2 - p1 + 1

    time_distance_pairs = [(int(info[0].split(':')[1]),
                           int(info[1].split(':')[1]))]
    print(time_distance_pairs)
    total = 1

    for pair in time_distance_pairs:
        total *= calculate_ways_to_win(pair)

    return total


# with open('small.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.read().replace(' ', '').split('\n')

print(solve(lines))
