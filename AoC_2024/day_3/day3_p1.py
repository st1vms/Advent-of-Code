"""AoC 2024 Day 3 Part 1 solution"""
import re

INPUT_FILE = "input.txt"

# Read input file
INPUT_STRING = None
with open(INPUT_FILE, "r", encoding='utf-8') as fp:
    INPUT_STRING = fp.read()

# Regex pattern
PATTERN = r"mul\((\d+),(\d+)\)"

# Find all valid multiplier instructions
matches = re.findall(PATTERN, INPUT_STRING)

# Calculate total multiplication value
TOTAL = 0
for match in matches:
    TOTAL += int(match[0])*int(match[1])

# Prints solution
print(f"Total multiplication: {TOTAL}")
