"""AoC 2024 Day 14 Part 2 solution"""

import re
import numpy as np

INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r", encoding="utf-8") as fp:
    aoc = np.array(
        [[*map(int, re.findall(r"-?\d+", line))] for line in fp.read().splitlines()]
    )

W, H, M = 101, 103, float("inf")

for r in range(1, W * H):
    aoc[:, :2] = (aoc[:, :2] + aoc[:, 2:]) % [W, H]
    p = np.prod(
        [
            np.sum((aoc[:, 0] < W // 2) & (aoc[:, 1] < H // 2)),
            np.sum((aoc[:, 0] > W // 2) & (aoc[:, 1] < H // 2)),
            np.sum((aoc[:, 0] < W // 2) & (aoc[:, 1] > H // 2)),
            np.sum((aoc[:, 0] > W // 2) & (aoc[:, 1] > H // 2)),
        ]
    )
    if p < M:
        M, part2 = p, r

# Prints solution
print(f"Seconds: {part2}")
