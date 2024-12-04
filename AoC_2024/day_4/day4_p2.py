"""AoC 2024 Day 4 Part 2 solution"""

INPUT_FILE = "input.txt"

# Read the input file
INPUT_MATRIX = []
with open(INPUT_FILE, "r", encoding="utf-8") as fp:
    for line in fp.readlines():
        INPUT_MATRIX.append(list(line.strip()))


def get_diagonals_neighbours_cells(
    matrix: list[list], x_start: int, y_start: int, n_cells: int
) -> list[list[str]]:
    """Returns a list of lists of at most `n_cells` neighbours
    starting at position `x_start` and `y_start` in the `matrix`"""

    directions = [
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


def count_x_word(input_matrix: list[list[str]], three_character_string: str) -> int:
    """Find total number of times a word is present in the input matrix"""
    total = 0
    for x, row in enumerate(input_matrix):
        for y, ch in enumerate(row):

            # Only count positions that have middle letter
            if ch != three_character_string[1]:
                continue

            diagonals_neigh = get_diagonals_neighbours_cells(input_matrix, x, y, 1)
            if not all(diagonals_neigh):
                continue

            top_left, top_right, btm_left, btm_right = diagonals_neigh

            # Diagonal check one
            if three_character_string == "".join(top_left) + ch + "".join(btm_right):
                if three_character_string == "".join(btm_left) + ch + "".join(
                    top_right
                ) or three_character_string == "".join(top_right) + ch + "".join(
                    btm_left
                ):
                    total += 1

            # Diagonal check two
            if three_character_string == "".join(btm_right) + ch + "".join(top_left):
                if three_character_string == "".join(btm_left) + ch + "".join(
                    top_right
                ) or three_character_string == "".join(top_right) + ch + "".join(
                    btm_left
                ):
                    total += 1
    return total


# Prints solution
print(f"Number of XMAS: {count_x_word(INPUT_MATRIX, 'MAS')}")
