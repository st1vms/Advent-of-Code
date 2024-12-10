"""AoC 2024 Day 8 Part 2 solution"""

from itertools import combinations

INPUT_FILE = "input.txt"


def read_map(input_file: str) -> list[list[str]]:
    """Reads antenna map as matrix of strings"""
    matrix = []
    with open(input_file, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            matrix.append([ch for ch in line.strip()])
    return matrix


def read_antennas_positions(map_matrix: list[list[str]]) -> dict[str, list[tuple[int]]]:
    """Reads antennas positions and save them in a dictionary"""
    antennas = {}

    for i, row in enumerate(map_matrix):
        for j, cell in enumerate(row):
            if cell == ".":
                continue
            if cell not in antennas:
                antennas[cell] = [(i, j)]
            else:
                antennas[cell] += [(i, j)]

    return antennas


def out_of_boundary(matrix: list[list], pos: tuple[int]) -> bool:
    """Return true if position is out of boundary"""
    return not (0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0]))


def find_antinode_positions(
    map_matrix: list[list[str]], positions: list[tuple[int]]
) -> list[tuple[int]]:
    """Finds possible antinode inside the map based off all similar antennas positions
    Returns a list of coordinates (x, y) for all the possible antinodes found,
    Empty list in case of no positions found"""

    antinodes = []
    # Create all combinations of positions pairs
    for position_pair in list(combinations(positions, 2)):

        # Find distance between the two points
        (x1, y1), (x2, y2) = position_pair
        distance = (x2 - x1, y2 - y1)

        # Find position of all antinodes in both directions
        sub_antinodes = []

        # Calculate the antinodes in both directions
        for k in range(1, max(len(map_matrix), len(map_matrix[0]))):
            # Find position of both antinodes
            if x1 == x2:  # Same row
                antinode_one = (x1, min(y1, y2) - k * distance[1])
                antinode_two = (x1, max(y1, y2) + k * distance[1])
            elif y1 == y2:  # Same column
                antinode_one = (min(x1, x2) - k * distance[0], y1)
                antinode_two = (max(x1, x2) + k * distance[0], y1)
            else:  # Diagonal
                antinode_one = (x1 - k * distance[0], y1 - k * distance[1])
                antinode_two = (x2 + k * distance[0], y2 + k * distance[1])

            if out_of_boundary(map_matrix, antinode_one) and out_of_boundary(
                map_matrix, antinode_two
            ):
                break

            sub_antinodes.append(antinode_one)
            sub_antinodes.append(antinode_two)

        for antinode in sub_antinodes:
            # Check if antinode one can be placed
            if (
                not out_of_boundary(map_matrix, antinode)
                and map_matrix[antinode[0]][antinode[1]] != "#"
            ):
                antinodes.append(antinode)

                # PLace the antinode
                map_matrix[antinode[0]][antinode[1]] = "#"

    return antinodes


def _main() -> None:

    # Read input
    antenna_map = read_map(INPUT_FILE)

    # Get antennas positions
    antennas_pos = read_antennas_positions(antenna_map)

    # Find solution
    antinode_pos = []
    for _, pos in antennas_pos.items():
        antinode_pos += find_antinode_positions(antenna_map, pos)

    # Also consider antennas with at least two other similar ones as antinodes
    for pos in antennas_pos.values():
        if len(pos) <= 2:
            continue
        for p in pos:
            if antenna_map[p[0]][p[1]] != "#":
                antinode_pos.append(p)

    # Prints solution
    print(f"Total number of unique antinode positions: {len(antinode_pos)}")


if __name__ == "__main__":
    _main()
