"""AoC 2024 Day 3 Part 2 solution"""

import re

INPUT_FILE = "input.txt"

# Read input file
INPUT_STRING = None
with open(INPUT_FILE, "r", encoding="utf-8") as fp:
    INPUT_STRING = fp.read()

# New Regex pattern to include do() and don't()
PATTERN = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

# Find all valid instructions
matches = re.finditer(PATTERN, INPUT_STRING)

# Process instructions

DO = True
TOTAL = 0
for match in matches:
    if match.group(1) and match.group(2):
        # It's a mul(x,y) pattern
        if DO:
            # Allowed multiplication
            TOTAL += int(match.group(1)) * int(match.group(2))
    elif match.group(0) == "do()":
        DO = True  # Enable next mult
    elif match.group(0) == "don't()":
        DO = False  # Disable next mult

# Prints solution
print(f"Total multiplication: {TOTAL}")
