"""AoC 2024 Day 9 Part 1 solution"""

INPUT_FILE = "input.txt"


def read_disk_map(input_file: str) -> list[int]:
    """Reads input file as a lit of integers"""

    data = []
    with open(input_file, "r", encoding="utf-8") as fp:
        for ch in fp.read():
            data.append(int(ch))

    if len(data) % 2 == 1:
        data.append(0) # Add padding

    return data


def get_files_and_gaps(disk_map: list[int]) -> tuple[list[int]]:
    """Returns list of files and gaps"""
    files, gaps = [], []
    head = 0
    for i in range(0, len(disk_map), 2):
        files.append((head, disk_map[i]))
        head += disk_map[i]
        gaps.append((head, disk_map[i + 1]))
        head += disk_map[i + 1]

    return files, gaps


def rearrange_blocks(files: list[int], gaps: list[int]) -> list[int]:
    """Rearramge files and returns a list with them"""

    for i in range(len(files) - 1, -1, -1):
        file_start, file_size = files[i]

        for j, gap in enumerate(gaps):
            gap_start, gap_size = gap
            if gap_start > file_start:
                break

            if gap_size >= file_size:
                file_start = gap_start
                gap_start = gap_start + file_size
                gap_size = gap_size - file_size

                files[i] = (file_start, file_size)
                gaps[j] = (gap_start, gap_size)
    return files


def calculate_checksum(files: list[int]) -> int:
    """Calculate checksum given the rearranged disk map"""

    checksum = 0
    for i, file in enumerate(files):
        file_start, file_size = file
        for j in range(file_start, file_start + file_size):
            checksum += i * j
    return checksum


def _main() -> None:

    # Read disk map
    disk_map = read_disk_map(INPUT_FILE)

    # Get files and gaps
    files, gaps = get_files_and_gaps(disk_map)

    # Rearrange file blocks
    files = rearrange_blocks(files, gaps)

    # Calculate checksum
    checksum = calculate_checksum(files)

    # Prints solution
    print(f"Checksum: {checksum}")


if __name__ == "__main__":
    _main()
