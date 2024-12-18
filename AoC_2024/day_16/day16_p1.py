"""AoC 2024 Day 16  Part 1 solution"""

import heapq
from dataclasses import dataclass

INPUT_FILE = "input.txt"


class AStar:
    """A star algorithm"""

    @dataclass
    class Cell:
        """Cell data"""

        parent_i = 0
        # Parent cell's column index
        parent_j = 0
        # Total cost of the cell (g + h)
        f = float("inf")
        # Cost from start to this cell
        g = float("inf")
        # Heuristic cost from this cell to destination
        h = 0

    def is_valid(self, grid, row, col):
        """Check if cell is out of bounds"""
        return (row >= 0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0]))

    def is_unblocked(self, grid, row, col):
        """Check if a cell is unblocked"""
        return grid[row][col] in "SE."

    def is_destination(self, row, col, dest):
        """Check if a cell is the destination"""
        return row == dest[0] and col == dest[1]

    def calculate_h_value(self, row, col, dest):
        """Calculate the heuristic value of a cell (Euclidean distance to destination)"""
        return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

    def trace_path(self, cell_details, dest) -> list[tuple[int]]:
        """Trace the path from source to destination"""
        path = []
        row = dest[0]
        col = dest[1]

        # Trace the path from destination to source using parent cells
        while not (
            cell_details[row][col].parent_i == row
            and cell_details[row][col].parent_j == col
        ):
            path.append((row, col))
            temp_row = cell_details[row][col].parent_i
            temp_col = cell_details[row][col].parent_j
            row = temp_row
            col = temp_col

        # Add the source cell to the path
        path.append((row, col))
        # Reverse the path to get the path from source to destination
        path.reverse()

        return path

    def search(self, grid, src, dest) -> list[tuple[int]]:
        """Implement the A* search algorithm"""
        # Check if the source and destination are valid
        if not self.is_valid(grid, src[0], src[1]) or not self.is_valid(
            grid, dest[0], dest[1]
        ):
            print("Source or destination is invalid")
            return

        # Check if the source and destination are unblocked
        if not self.is_unblocked(grid, src[0], src[1]) or not self.is_unblocked(
            grid, dest[0], dest[1]
        ):
            print("Source or the destination is blocked")
            return

        # Check if we are already at the destination
        if self.is_destination(src[0], src[1], dest):
            print("We are already at the destination")
            return

        # Initialize the closed list (visited cells)
        closed_list = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # Initialize the details of each cell
        cell_details = [
            [AStar.Cell() for _ in range(len(grid[0]))] for _ in range(len(grid))
        ]

        # Initialize the start cell details
        i = src[0]
        j = src[1]
        cell_details[i][j].f = 0
        cell_details[i][j].g = 0
        cell_details[i][j].h = 0
        cell_details[i][j].parent_i = i
        cell_details[i][j].parent_j = j

        # Initialize the open list (cells to be visited) with the start cell
        open_list = []
        heapq.heappush(open_list, (0.0, i, j))

        directions = [
            (0, 1),  # Right
            (1, 0),  # Down
            (0, -1),  # Left
            (-1, 0),  # Up
        ]

        # Main loop of A* search algorithm
        while len(open_list) > 0:
            # Pop the cell with the smallest f value from the open list
            p = heapq.heappop(open_list)

            # Mark the cell as visited
            i, j = p[1], p[2]
            closed_list[i][j] = True

            # Generate successors based on clockwise rule
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]

                # If the successor is valid, unblocked, and not visited
                if (
                    self.is_valid(grid, new_i, new_j)
                    and self.is_unblocked(grid, new_i, new_j)
                    and not closed_list[new_i][new_j]
                ):
                    # If the successor is the destination
                    if self.is_destination(new_i, new_j, dest):
                        # Set the parent of the destination cell
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j
                        print("The destination cell is found")
                        # Trace and print the path from source to destination
                        return self.trace_path(cell_details, dest)
                    # Calculate the new f, g, and h values
                    g_new = cell_details[i][j].g + 1.0
                    h_new = self.calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                    if (
                        cell_details[new_i][new_j].f == float("inf")
                        or cell_details[new_i][new_j].f > f_new
                    ):
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        # Update the cell details
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j

        return []


def _pretty_print_path(matrix: list[list[str]], path: list[tuple[int]]):

    new_matrix = [list(row) for row in matrix]
    for p in path:
        new_matrix[p[0]][p[1]] = "O"

    for row in new_matrix:
        for cell in row:
            print(cell, end="")
        print("")


def read_input(input_file: str) -> list[list[str]]:
    """Reads input map file as matrix"""

    matrix = []

    with open(input_file, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            matrix.append(list(line.strip()))

    return matrix


def find_src_and_dst(matrix_map: list[list[str]]) -> tuple[tuple[int]]:
    """Find source and destination coordinates"""
    src = None
    dst = None
    for i, row in enumerate(matrix_map):
        for j, cell in enumerate(row):
            if cell == "E":
                dst = (i, j)
            elif cell == "S":
                src = (i, j)
    return src, dst


def calculate_score(path: tuple[int]) -> None:
    """Calculate score based off path"""

    score = 0
    prev_x, prev_y = path[0]
    prev_direction = None
    for coord in path[1:]:
        x, y = coord

        score += 1

        if x == prev_x + 1 and y == prev_y:
            direction = 0
        elif x == prev_x - 1 and y == prev_y:
            direction = 1
        elif x == prev_x and y == prev_y + 1:
            direction = 2
        elif x == prev_x and y == prev_y - 1:
            direction = 3

        if prev_direction is not None:
            if prev_direction != direction:
                score += 1000
        prev_direction = direction

        prev_x, prev_y = x, y

    return score


def _main() -> None:
    # Reads input
    matrix_map = read_input(INPUT_FILE)

    src, dst = find_src_and_dst(matrix_map)

    astar = AStar()

    path = astar.search(matrix_map, src, dst)

    score = calculate_score(path)

    # Prints solution
    print(f"Best path score: {score}")
    _pretty_print_path(matrix_map, path)


if __name__ == "__main__":
    _main()
