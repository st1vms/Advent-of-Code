"""AoC 2024 Day 5 Part 2 solution"""
from collections import defaultdict, deque

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
        for num in update_line.split(","):
            update.append(int(num))
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


def fix_update(array: list[int]) -> list[int]:
    """Fix the update and returns it"""

    # Build the dependency graph only for the relevant pages in this update
    in_degree = {page: 0 for page in update}
    graph = defaultdict(list)

    for page in update:
        if page in RULES:
            for dependency in RULES[page]:
                if dependency in update:  # Only include dependencies in the update
                    graph[dependency].append(page)
                    in_degree[page] += 1

    # Perform topological sort using Kahn's Algorithm
    sorted_pages = []
    queue = deque([page for page in update if in_degree[page] == 0])

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages


# Get correct updates
uncorrect_updates = []
for update in UPDATES:
    if not is_correct(update):
        uncorrect_updates.append(fix_update(update))  # Add the fixed update

# Get middle numbers from correct updates
middle_nums = []
for update in uncorrect_updates:
    middle_nums.append(update[len(update) // 2])

# Prints solution
print(f"Total sum of middle numbers: {sum(middle_nums)}")
