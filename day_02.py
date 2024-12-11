import os
from collections import Counter

is_sorted = lambda row: row == sorted(row)


def is_safe(row):
    if not is_sorted(row) and not is_sorted(row[::-1]):
        return False
    if len(set(row)) != len(row):
        return False
    return max(abs(a - b) for a, b in zip(row, row[1:])) <= 3


def read_input():
    with open("day_02.txt") as f:
        rows = []
        for line in f:
            rows += [list(map(int, line.strip().split()))]
        return rows


def solve_part_1(rows):
    return sum([is_safe(row) for row in rows])


def solve_part_2(rows):
    def is_safe_2(row):
        return is_safe(row) or any(
            is_safe(row[:i] + row[i + 1 :]) for i in range(len(row))
        )
    return sum([is_safe_2(row) for row in rows])


if __name__ == "__main__":
    rows = read_input()
    print(solve_part_1(rows))
    print(solve_part_2(rows))
