"""AoC 2024 Day 15 Part 1 solution"""

INPUT_FILE = "input.txt"

DIRECTIONS = {
    "^": (-1, 0),  # Up
    ">": (0, 1),  # Right
    "v": (1, 0),  # Down
    "<": (0, -1),  # Left
}


def _pretty_print(matrix: list[list[str]]):

    for row in matrix:
        for cell in row:
            print(cell, end="")
        print("")


def read_input(input_file: str) -> tuple[list[list[str]], list[str]]:
    """Reads input map and moves list from file"""
    matrix = []
    moves = []

    with open(input_file, "r", encoding="utf-8") as fp:
        matrix_text, moves_text = fp.read().strip().split("\n\n")

        for row in matrix_text.split("\n"):
            matrix.append(list(row))

        for move in moves_text:
            moves.append(move)

    return matrix, moves


def find_robot_pos(matrix_map: list[list[str]]) -> tuple[int] | None:
    """Return robot coordinates in the map"""

    for i, row in enumerate(matrix_map):
        for j, cell in enumerate(row):
            if cell == "@":
                return (i, j)
    return None


def get_walk_position(x: int, y: int, move: str) -> tuple[int, int]:
    """Get the next position based off starting position and direction"""
    return (x + DIRECTIONS[move][0], y + DIRECTIONS[move][1])


def move_robot(matrix_map: list[list[str]], move: str) -> list[list[str]]:
    """Moves robot according to moves and updates map with pushed boxes"""
    return  matrix_map

def calculate_gps_sum(matrix_map: list[list[str]]) -> int:
    """Calculate the sum of GPS coordinates for all boxes"""
    gps_sum = 0
    for i, row in enumerate(matrix_map):
        for j, cell in enumerate(row):
            if cell == "O":
                gps_sum += (100 * i) + j
    return gps_sum

def _main() -> None:
    # Reads input
    matrix_map, moves = read_input(INPUT_FILE)

    # Simulate moves
    for move in moves:
        matrix_map = move_robot(matrix_map, move)

    # Calculate and print the GPS sum
    gps_sum = calculate_gps_sum(matrix_map)
    print(gps_sum)


if __name__ == "__main__":
    _main()
