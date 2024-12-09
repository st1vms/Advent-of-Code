"""AoC 2024 Day 9 Part 1 solution"""

INPUT_FILE = "input.txt"


def read_disk_map(input_file: str) -> str:
    """Reads input file as a single string"""
    with open(input_file, "r", encoding="utf-8") as fp:
        return fp.read().strip()


def convert_disk_map(disk_map: str) -> list[int]:
    """Convert disk map into its long form"""

    spaced = []
    for i, letter in enumerate(disk_map):
        num = int(letter)
        index = int(i) // 2
        for _ in range(num):
            if i % 2 == 0:
                spaced.append(index)
            else:
                spaced.append(-1)
    return spaced


def move_blocks(spaced_disk_map: list[int]) -> list[int]:
    """Rearrange blocks to occupy leftmost free space"""
    compacted = []
    for _, i in enumerate(spaced_disk_map):
        if i == -1:
            while True:
                a = spaced_disk_map.pop()
                if a != -1:
                    compacted.append(a)
                    break
        else:
            compacted.append(i)
    return compacted


def calculate_checksum(disk_map: str) -> int:
    """Calculate checksum given the rearranged disk map"""

    checksum = 0

    for i, ch in enumerate(disk_map):
        if ch == ".":
            break
        checksum += i * int(ch)

    return checksum


def _main() -> None:

    # Read disk map
    disk_map = read_disk_map(INPUT_FILE)

    # Convert it to long form
    long_disk_map = convert_disk_map(disk_map)

    # Rearrange blocks to fill leftmost free space
    rearranged_disk_map = move_blocks(long_disk_map)

    # Calculate checksum
    checksum = calculate_checksum(rearranged_disk_map)

    # Prints solution
    print(f"Checksum: {checksum}")


if __name__ == "__main__":
    _main()
