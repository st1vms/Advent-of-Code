"""AoC 2024 Day 5 Part 1 solution"""

INPUT_FILE = "input.txt"

# Read the input file
RULES: dict[int, set[int]] = {}
UPDATES = []
with open(INPUT_FILE, "r", encoding="utf-8") as fp:
    rules_text, updates_text = fp.read().strip().split("\n\n")

    # Read rules text
    for rule_line in rules_text.split("\n"):
        X, Y = rule_line.split("|")
        X, Y = int(X), int(Y)
        if X not in RULES:
            RULES[X] = set([Y])
        else:
            RULES[X].add(Y)

    # Read updates text part
    for update_line in updates_text.split("\n"):
        update = []
        for page in update_line.split(","):
            update.append(int(page))
        UPDATES.append(update)


def is_correct(array: list[int]) -> bool:
    """Determine if an update is correct by applying rules"""

    for i, a in enumerate(array):

        # Applies rules to character in X set
        if a not in RULES:
            continue

        for b in array[:i]:
            # b is behind a
            if b in RULES[a]:
                # a must be behind b
                return False
    return True


# Get correct updates
correct_updates = []
for update in UPDATES:
    if is_correct(update):
        correct_updates.append(update)

# Get middle numbers from correct updates
middle_nums = []
for update in correct_updates:
    middle_nums.append(update[len(update) // 2])

# Prints solution
print(f"Total sum of middle numbers: {sum(middle_nums)}")
