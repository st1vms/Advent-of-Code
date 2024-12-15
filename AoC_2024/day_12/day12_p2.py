"""AoC 2024 Day 12 Part 2 solution"""

INPUT_FILE = "input.txt"

DIRECTIONS = +1, -1, -1j, +1j


def read_input(file_path: str) -> dict[complex, str]:
    """Reads the input map from the given file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return {
            r + c * 1j: char
            for r, line in enumerate(file.readlines())
            for c, char in enumerate(line.strip())
        }


def neighbours(cell: complex) -> set[complex]:
    """Get neighbour cells"""
    return {cell + delta for delta in DIRECTIONS}


def region_neighbours(grid: dict[complex, str], cells: set[complex]) -> set[complex]:
    """Get neighbouring cells of a region"""
    return {
        neighbour
        for cell in cells
        for neighbour in neighbours(cell)
        if grid.get(neighbour) == grid.get(cell)
    }


def regions(grid: dict[complex, str]):
    """Generate regions from the grid"""
    unvisited = set(grid)
    while unvisited:
        seed = unvisited.pop()
        frontier = {seed}
        region = {seed}
        while frontier:
            frontier = region_neighbours(grid, frontier) & unvisited
            region |= frontier
            unvisited -= frontier
        yield region


def perimeter(region: set[complex]) -> int:
    """Calculate the perimeter of a region"""
    return sum(
        neighbour not in region for cell in region for neighbour in neighbours(cell)
    )


def corners(region: set[complex]) -> int:
    """Calculate the corners of a region"""
    inner = 0
    outer = 0
    for cell in region:
        for forward in DIRECTIONS:
            leftward = 1j * forward
            front = cell + forward
            left = cell + leftward
            diag = cell + forward + leftward
            cells = {cell, front, left, diag} & region
            if cells == {cell}:
                outer += 1
            if cells == {cell, front, left}:
                inner += 1
            if cells == {cell, diag}:
                inner += 1
    assert (inner - outer) % 4 == 0
    return inner + outer


def _main() -> None:
    """Main function to execute the solution"""

    # Reads input file
    grid = read_input(INPUT_FILE)

    # Get solution
    total_price = sum(len(region) * corners(region) for region in regions(grid))

    # Prints solution
    print(f"The total price of fencing all regions is: {total_price}")


if __name__ == "__main__":
    _main()
