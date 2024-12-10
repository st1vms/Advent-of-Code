"""AoC 2024 Day 6 Part 2 solution"""

import time

INPUT_FILE = "input.txt"

# Use Clockwise rotation
DIRECTIONS = {
    0: (-1, 0),  # Up
    1: (0, 1),  # Right
    2: (1, 0),  # Down
    3: (0, -1),  # Left
}


def read_map() -> list[list]:
    """Reads the map file into a matrix"""
    map_matrix = []
    with open(INPUT_FILE, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            row = []
            line = line.strip()
            for ch in line:
                if ch == ".":
                    # Free cell
                    row.append(".")
                elif ch == "#":
                    # Obstacle
                    row.append("#")
                elif ch == "^":
                    # Player facing up
                    row.append(0)
                elif ch == ">":
                    # Player facing right
                    row.append(1)
                elif ch == "V":
                    # Player facing down
                    row.append(2)
                elif ch == "<":
                    # Player facing left
                    row.append(3)
            map_matrix.append(row)
    return map_matrix


def find_player_position(
    map_matrix: list[list],
) -> tuple[int, int]:
    """Returns a tuple with (starting_position, starting_direction)"""
    pos = None
    for i, row in enumerate(map_matrix):
        for j, cell in enumerate(row):
            if not str(cell).isdigit():
                continue
            pos = (i, j)
            break
        if pos is not None:
            break
    return pos


def is_out_of_bounds(map_matrix: list[list], x: int, y: int) -> bool:
    """Check if position is out of bounds of matrix"""
    if 0 <= x < len(map_matrix) and 0 <= y < len(map_matrix[0]):
        return False
    return True


def get_walk_position(x: int, y: int, direction: int) -> tuple[int, int]:
    """Get the next position based off starting position and direction"""
    return (x + DIRECTIONS[direction][0], y + DIRECTIONS[direction][1])


def get_path_to_out_of_bounds(
    map_matrix: list[list], start_dir: int, start_pos: tuple[int, int]
) -> list[tuple[int]]:
    """Makes the character walk around map, avoiding obstacles,
    and returns a list of coordinates, once the character reaches the edges of the map
    """

    # Path coordinates
    coords = []

    prev_x, prev_y = start_pos
    while True:

        # Get next position based off direction
        new_x, new_y = get_walk_position(prev_x, prev_y, start_dir)
        if is_out_of_bounds(map_matrix, new_x, new_y):
            # Set the current position as the last path coordinates
            coords.append((prev_x, prev_y))
            break

        item = map_matrix[new_x][new_y]
        # Obstacle check
        if item == "#":
            # Obstacle found, rotate direction
            start_dir += 1
            if start_dir > 3:
                start_dir = 0
            if start_dir >= len(DIRECTIONS):
                start_dir = 0
            continue

        # Set the current position as the next path coordinates
        coords.append((prev_x, prev_y))
        prev_x, prev_y = new_x, new_y

    return coords


def find_possible_obstacles_coords(map_matrix: list[list]) -> list[tuple[int, int]]:
    """Given a player position, return all possible coordinates to place an obstacle"""
    coords = []
    for i, row in enumerate(map_matrix):
        for j, value in enumerate(row):
            if str(value).isdigit():
                continue
            if value == "#":
                continue
            coords.append((i, j))
    return coords


def find_loop(
    map_matrix: list[list], start_dir: int, start_pos: tuple[int, int]
) -> bool:
    """Returns true if this path makes the player move in a loop"""

    visited_pos = set()
    prev_x, prev_y = start_pos
    while True:

        # Get next position based off direction
        new_x, new_y = get_walk_position(prev_x, prev_y, start_dir)
        if is_out_of_bounds(map_matrix, new_x, new_y):
            # Loop not found
            return False

        item = map_matrix[new_x][new_y]
        # Obstacle check
        if item == "#":
            # Obstacle found, rotate direction
            start_dir += 1
            if start_dir > 3:
                start_dir = 0
            if start_dir >= len(DIRECTIONS):
                start_dir = 0
            continue

        # Set the current position as the next path coordinates
        prev_x, prev_y = new_x, new_y

        # Loop check
        if (prev_x, prev_y, start_dir) in visited_pos:
            return True

        visited_pos.add((prev_x, prev_y, start_dir))


if __name__ == "__main__":

    # Read the map file
    MAP = read_map()

    # Get possible obstacles coordinates
    obst_coords = find_possible_obstacles_coords(MAP)

    # Get starting position and starting direction of player
    START_POS = find_player_position(MAP)
    START_DIR = MAP[START_POS[0]][START_POS[1]]

    LOOP_COUNT = 0
    for coord in obst_coords:

        # Try adding this obstacle
        NEW_MAP = [row[:] for row in MAP]
        NEW_MAP[coord[0]][coord[1]] = "#"
        if find_loop(NEW_MAP, START_DIR, START_POS):
            LOOP_COUNT += 1

    # Prints solution
    print(f"Loop count: {LOOP_COUNT}")
