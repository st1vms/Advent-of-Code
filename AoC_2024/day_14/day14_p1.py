"""AoC 2024 Day 14 Part 1 solution"""

INPUT_FILE = "input.txt"


def read_input(filename):
    robots = []
    with open(filename, "r") as file:
        for line in file:
            # Split the line into position and velocity parts
            position_part, velocity_part = line.strip().split(" v=")

            # Extract the position and velocity
            position = tuple(
                map(int, position_part[2:].split(","))
            )  # remove "p=" and split by comma
            velocity = tuple(map(int, velocity_part.split(",")))  # split by comma

            robots.append((position, velocity))

    return robots


def simulate_robots(robots, time_steps):
    # Initialize a grid of size 101x103
    grid_width = 101
    grid_height = 103
    grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]

    # Simulate robot movements
    for p, v in robots:
        x, y = p
        vx, vy = v

        # Calculate new position after time_steps seconds with wrapping
        x_new = (x + vx * time_steps) % grid_width
        y_new = (y + vy * time_steps) % grid_height

        # Mark the robot's new position on the grid
        grid[y_new][x_new] += 1

    return grid


def calculate_safety_factor(grid):
    # Define center positions for 101x103 grid (central row and column)
    center_x = 50  # Half of 101 is 50 (indexing starts at 0)
    center_y = 51  # Half of 103 is 51 (indexing starts at 0)

    # Count robots in the quadrants
    top_left = top_right = bottom_left = bottom_right = 0

    for y in range(103):
        for x in range(101):
            if x == center_x or y == center_y:
                continue  # Skip the middle row and column
            if x < center_x and y < center_y:
                top_left += grid[y][x]
            elif x >= center_x and y < center_y:
                top_right += grid[y][x]
            elif x < center_x and y >= center_y:
                bottom_left += grid[y][x]
            elif x >= center_x and y >= center_y:
                bottom_right += grid[y][x]

    # Safety factor is the product of robots in each quadrant
    safety_factor = top_left * top_right * bottom_left * bottom_right
    return safety_factor


def _main() -> None:

    # Reads input file
    robots = read_input(INPUT_FILE)

    # Simulate the robots' positions after 100 seconds
    grid = simulate_robots(robots, 100)

    # Calculate the safety factor
    safety_factor = calculate_safety_factor(grid)

    # Prints solution
    print(f"Safety factor: {safety_factor}")


if __name__ == "__main__":
    _main()
