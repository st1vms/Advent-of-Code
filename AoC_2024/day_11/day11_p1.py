"""AoC 2024 Day 11 Part 1 solution"""

INPUT_FILE = "input.txt"


def get_input_stones(input_file: str) -> list[str]:
    """Return list of stones with their number as a string"""

    stones = []
    with open(input_file, "r", encoding="utf-8") as fp:
        stones = fp.read().strip().split(" ")
    return stones


def blink(stones: list[str]) -> list[str]:
    """Perform blink logic to change stones"""
    new_stones = []

    for stone in stones:
        # Apply blink rules

        stone_int = int(stone)
        if stone_int == 0:
            # Flip zero
            new_stones.append("1")
            continue

        if len(stone) % 2 == 0:
            # Split number
            mid = len(stone) // 2
            left, right = stone[:mid], stone[mid:]
            # Avoid multiple 0 by converting to int and then to str
            new_stones.append(str(int(left)))
            new_stones.append(str(int(right)))
            continue

        # Multiply stone value by 2024
        new_stones.append(str(stone_int * 2024))
    return new_stones


def _main() -> None:

    # Times to blink
    n_blinks = 25

    # Get stones from input file
    stones = get_input_stones(INPUT_FILE)

    # Blink N times, getting the new stones
    new_stones = stones
    for _ in range(n_blinks):
        new_stones = blink(new_stones)

    # Prints solution
    print(f"Number of stones after {n_blinks} blinks: {len(new_stones)}")


if __name__ == "__main__":
    _main()
