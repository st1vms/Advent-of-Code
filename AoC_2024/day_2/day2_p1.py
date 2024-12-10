"""AoC 2024 Day 2 Part 1 solution"""

INPUT_FILE = "input.txt"


def is_decreasing(report: list[int]) -> bool:
    """Check if levels are decreasing,
    with no more than three digits of difference"""

    prev_level = report[0]
    for level in report[1:]:
        if prev_level > level:
            # Extra condition for report safety
            if prev_level - level <= 3:
                prev_level = level
                continue
        return False
    return True


def is_increasing(report: list[int]) -> bool:
    """Check if levels are increasing,
    with no more than three digits of difference"""

    prev_level = report[0]
    for level in report[1:]:
        if prev_level < level:
            # Extra condition for report safety
            if level - prev_level <= 3:
                prev_level = level
                continue
        return False
    return True


def is_report_safe(report: list[int]) -> bool:
    """Return True if report is safe"""
    return is_increasing(report) or is_decreasing(report)


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
