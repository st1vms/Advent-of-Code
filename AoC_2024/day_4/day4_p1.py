"""AoC 2024 Day 4 Part 1 solution"""

INPUT_FILE = "input.txt"

# Read the input file
INPUT_MATRIX = []
with open(INPUT_FILE, "r", encoding="utf-8") as fp:
    for line in fp.readlines():
        INPUT_MATRIX.append(list(line.strip()))


def get_neighbor_cells(
    matrix: list[list], x_start: int, y_start: int, n_cells: int
) -> list[list[str]]:
    """Returns a list of 8 lists of at most `n_cells` neighbours
    starting at position `x_start` and `y_start` in the `matrix`"""

    directions = [
        (-1, 0),  # Up
        (1, 0),  # Down
        (0, -1),  # Left
        (0, 1),  # Right
        (-1, -1),  # Top-left
        (-1, 1),  # Top-right
        (1, -1),  # Bottom-left
        (1, 1),  # Bottom-right
    ]
    neighbors = []
    rows, cols = len(matrix), len(matrix[0])

    for dx, dy in directions:
        sub_neighbors = []
        for distance in range(1, n_cells + 1):
            new_x, new_y = x_start + dx * distance, y_start + dy * distance

            # Boundary check
            if 0 <= new_x < rows and 0 <= new_y < cols:
                sub_neighbors.append(matrix[new_x][new_y])
            else:
                # Out of bounds
                break
        neighbors.append(sub_neighbors)
    return neighbors


def count_words(input_matrix: list[list[str]], target_word: str) -> int:
    """Find total number of times a word is present in the input matrix"""
    total = 0
    for x, row in enumerate(input_matrix):
        for y, ch in enumerate(row):

            # Only count positions that have the first letter
            if ch != target_word[0]:
                continue

            # Get neighbours cells
            neighbours = get_neighbor_cells(input_matrix, x, y, len(target_word) - 1)

            # Iterate through directions
            for direction in neighbours:
                if not direction or len(direction) < len(target_word) - 1:
                    # Discard empty directions or smaller than expected
                    continue

                # Check if word is found in this direction
                if target_word[1:] == "".join(direction):
                    # Increment total
                    total += 1
    return total


# Prints solution
print(f"Number of XMAS: {count_words(INPUT_MATRIX, 'XMAS')}")
