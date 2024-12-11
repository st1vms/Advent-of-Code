"""AoC 2024 Day 11 Part 2 solution"""
from collections import Counter

INPUT_FILE = "input.txt"


def get_input_stones(input_file: str) -> list[int]:
    """Return list of stones with their number as a string"""

    stones = []
    with open(input_file, "r", encoding="utf-8") as fp:
        for ch in fp.read().strip().split(" "):
            stones.append(int(ch))
    return stones


def count_stones_after_blinks(initial_stones:list[int], blinks:int):
    """Count the amount of stones after N blinks"""

    def process_stone(stone):
        """Applies the transformation rules to a single stone."""
        if stone == 0:
            return [1]
        if len(str(stone)) % 2 == 0:
            digits = str(stone)
            mid = len(digits) // 2
            left = int(digits[:mid])
            right = int(digits[mid:])
            return [left, right]
        return [stone * 2024]

    # Use a counter to track how many of each type of stone exists
    stone_counts = Counter(initial_stones)

    for _ in range(blinks):
        next_stone_counts = Counter()
        for stone, count in stone_counts.items():
            transformed_stones = process_stone(stone)
            for transformed_stone in transformed_stones:
                next_stone_counts[transformed_stone] += count
        stone_counts = next_stone_counts

    return sum(stone_counts.values())


def _main() -> None:

    # Times to blink
    n_blinks = 75

    # Get stones from input file
    stones = get_input_stones(INPUT_FILE)

    # Calculate the number of stones
    result = count_stones_after_blinks(stones, n_blinks)

    # Prints solution
    print(f"Number of stones after {n_blinks} blinks: {result}")


if __name__ == "__main__":
    _main()
