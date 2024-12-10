"""AoC 2024 Day 10 Part 1 solution"""

INPUT_FILE = "input.txt"

DIRECTIONS = {
    "top": (-1, 0),  # Up
    "right": (0, 1),  # Right
    "bottom": (1, 0),  # Down
    "left": (0, -1),  # Left
}


def read_map(input_file: str) -> list[list[int]]:
    """Reads puzzle input map from file"""
    matrix = []
    with open(input_file, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            row = []
            for ch in line.strip():
                if ch == ".":
                    row.append(-1)
                    continue
                row.append(int(ch))
            matrix.append(row)
    return matrix


def is_out_of_bounds(map_matrix: list[list], x: int, y: int) -> bool:
    """Check if position is out of bounds of matrix"""
    if 0 <= x < len(map_matrix) and 0 <= y < len(map_matrix[0]):
        return False
    return True


def get_walk_position(x: int, y: int, direction: str) -> tuple[int, int]:
    """Get the next position based off starting position and direction"""
    return (x + DIRECTIONS[direction][0], y + DIRECTIONS[direction][1])


def __pretty_print_map(matrix: list[list]):

    for row in matrix:
        for cell in row:
            if cell == -1:
                print(".", end="")
            else:
                print(cell, end="")
        print("")


def find_nearby_cell_pos(
    topo_map: list[list[int]], start_pos: tuple[int], value: int
) -> list[tuple[int]]:
    """Finds nearby cell positions in all directions based off value, returns list of coordinates"""
    pos = []

    x, y = start_pos

    top = get_walk_position(x, y, "top")
    bottom = get_walk_position(x, y, "bottom")
    left = get_walk_position(x, y, "left")
    right = get_walk_position(x, y, "right")

    if (
        not is_out_of_bounds(topo_map, top[0], top[1])
        and topo_map[top[0]][top[1]] == value
    ):
        pos.append(top)

    if (
        not is_out_of_bounds(topo_map, bottom[0], bottom[1])
        and topo_map[bottom[0]][bottom[1]] == value
    ):
        pos.append(bottom)

    if (
        not is_out_of_bounds(topo_map, left[0], left[1])
        and topo_map[left[0]][left[1]] == value
    ):
        pos.append(left)

    if (
        not is_out_of_bounds(topo_map, right[0], right[1])
        and topo_map[right[0]][right[1]] == value
    ):
        pos.append(right)

    return pos


def get_trailheads_positions(topo_map: list[list[int]]) -> list[tuple[int]]:
    """Get traileahds coordinates inside the map matrix"""
    pos = []

    for i, row in enumerate(topo_map):
        for j, cell in enumerate(row):
            if cell == 0:
                pos.append((i, j))
    return pos


def get_trailhead_score(topo_map: list[list[int]], start_pos: tuple[int]) -> int:
    """Given a trailhead postion, returns the score"""

    score = 0

    stack = [start_pos]
    visited = set()

    while stack:
        current_pos = stack.pop()
        x, y = current_pos

        if current_pos in visited:
            continue

        visited.add(current_pos)

        if topo_map[x][y] == 9:
            score += 1
            continue

        next_value = topo_map[x][y] + 1
        nearby_cells = find_nearby_cell_pos(topo_map, current_pos, next_value)

        for cell in nearby_cells:
            if cell not in visited:
                stack.append(cell)

    return score


def _main() -> None:

    # Reads the input map
    topo_map = read_map(INPUT_FILE)

    # Get trailheads positions
    trailhads_pos = get_trailheads_positions(topo_map)

    # Calculate all the scores from the trailheads positions
    all_scores = []
    for pos in trailhads_pos:
        score = get_trailhead_score(topo_map, pos)
        all_scores.append(score)
        print(f"Trailhead {pos} score: {score}")

    # Prints solution
    print(f"Total score: {sum(all_scores)}")


if __name__ == "__main__":
    _main()
