"""AoC 2024 Day 2 Part 2 solution"""

INPUT_FILE = "input.txt"


def is_decreasing(report: list[int]) -> list[int]:
    """Check if levels are decreasing,
    with no more than three digits of difference,
    returns bad indexes"""

    # Holds indexes of bad levels
    bad_levels = []

    prev_level = report[0]
    for i, level in enumerate(report[1:]):
        if prev_level > level:
            # Extra condition for report safety
            if prev_level - level <= 3:
                prev_level = level
                continue

        # Bad index found, save it
        bad_levels.append(i)
        if i == len(report[1:]) - 1:
            # Also save last index
            bad_levels.append(i + 1)
        prev_level = level

    return bad_levels


def is_increasing(report: list[int]) -> list[int]:
    """Check if levels are increasing,
    with no more than three digits of differencee,
    returns bad indexes"""

    # Holds indexes of bad levels
    bad_levels = []

    prev_level = report[0]
    for i, level in enumerate(report[1:]):
        if prev_level < level:
            # Extra condition for report safety
            if level - prev_level <= 3:
                prev_level = level
                continue

        # Bad index found, save it
        bad_levels.append(i)
        if i == len(report[1:]) - 1:
            # Also save last index
            bad_levels.append(i + 1)
        prev_level = level

    return bad_levels


def is_report_safe(report: list[int]) -> bool:
    """Return True if report is safe"""

    # Get bad indexes from report
    bad_levels_increasing = is_increasing(report)
    bad_levels_decreasing = is_decreasing(report)

    # Check if report is already safe
    if len(bad_levels_increasing) == 0 or len(bad_levels_decreasing) == 0:
        return True

    # Applies "Problem Dampener" logic

    for bad_level in bad_levels_increasing:
        new_report = report.copy()
        new_report.pop(bad_level)
        if len(is_increasing(new_report)) == 0:
            # Removing one bad index makes the report safe
            return True

    for bad_level in bad_levels_decreasing:
        new_report = report.copy()
        new_report.pop(bad_level)
        if len(is_decreasing(new_report)) == 0:
            # Removing one bad index makes the report safe
            return True

    # Report is unsafe
    return False


# Read reports from input file
reports = []
with open(INPUT_FILE, "r", encoding="utf-8") as fp:
    for line in fp.readlines():
        # Load levels for each report
        # Remove extra whitespaces and newline
        levels = [int(c) for c in list(filter(bool, line.strip().split(" ")))]
        # Add report
        reports.append(levels)

# Get the safe reports
safe_reports = [report for report in reports if is_report_safe(report)]

# Prints solution
print(f"Number of safe reports: {len(safe_reports)}")
