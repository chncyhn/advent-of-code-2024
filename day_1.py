import os
from collections import Counter


def read_input():
    with open("day_1.txt") as f:
        rows = []
        for line in f:
            rows += [list(map(int, line.strip().split()))]
        return rows


def solve_part_1(rows):
    A = list(sorted([r[0] for r in rows]))
    B = list(sorted([r[1] for r in rows]))
    return sum([abs(a - b) for a, b in zip(A, B)])


def solve_part_2(rows):
    A = [r[0] for r in rows]
    B_cnts = Counter([r[1] for r in rows])
    ret = 0
    for a in A:
        ret += a * B_cnts[a]
    return ret


if __name__ == "__main__":
    rows = read_input()

    print(solve_part_1(rows))
    print(solve_part_2(rows))
