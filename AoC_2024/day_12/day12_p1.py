"""AoC 2024 Day 12 Part 1 solution"""

from itertools import product

INPUT_FILE = "input.txt"


def read_input(file_path: str) -> list[str]:
    """Reads the input map from the given file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


def calculate_area_and_perimeter(
    grid: list[str], x: int, y: int, visited: set[tuple[int]]
) -> tuple[int]:
    """Calculates the area and perimeter of a region using BFS."""

    plant_type = grid[x][y]
    queue = [(x, y)]
    visited.add((x, y))

    area = 0
    perimeter = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy = queue.pop(0)
        area += 1

        for dx, dy in directions:

            # Find neighbours
            nx, ny = cx + dx, cy + dy

            # Check if in bounds of grid
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):

                # Check if neighbour is the same plant type,
                # and it's not visisted
                if grid[nx][ny] == plant_type and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                elif grid[nx][ny] != plant_type:
                    perimeter += 1
            else:
                perimeter += 1

    return area, perimeter


def calculate_total_price(grid: list[str]) -> int:
    """Calculates the total price of fencing all regions on the map"""
    visited = set()
    total_price = 0

    for x, y in product(range(len(grid)), range(len(grid[0]))):
        if (x, y) not in visited:
            area, perimeter = calculate_area_and_perimeter(grid, x, y, visited)
            total_price += area * perimeter

    return total_price


def _main() -> None:
    grid = read_input(INPUT_FILE)
    total_price = calculate_total_price(grid)
    print(f"The total price of fencing all regions is: {total_price}")


if __name__ == "__main__":
    _main()
