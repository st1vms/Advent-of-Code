"""AoC 2024 Day 1 Part 2 solution"""

INPUT_FILE = "input.txt"

# Read lists
first_list = []
second_list = []
with open(INPUT_FILE, "r", encoding='utf-8') as fp:
    for line in fp.readlines():
        # Remove extra whitespaces and newline
        nums = list(filter(bool, line.strip().split(" ")))
        first_list.append(int(nums[0]))
        second_list.append(int(nums[1]))

# Calculate similarity score
scores = []
for a in first_list:
    c = second_list.count(a)
    scores.append(a * c)

# Prints solution
print(f"Total score is: {sum(scores)}")
