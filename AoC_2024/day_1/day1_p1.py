"""AoC 2024 Day 1 Part 1 solution"""

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

# Sort lists
first_list = sorted(first_list)
second_list = sorted(second_list)

# Calculate distances
distances = []
for a, b in zip(first_list, second_list):
    distances.append(abs(b-a))

# Prints solution
print(f"Total distance is: {sum(distances)}")
