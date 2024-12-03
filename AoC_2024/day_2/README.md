# AoC 2024 [Day 2](https://adventofcode.com/2024/day/2)

## Part 1

Solution file: [Part 1 solution](day2_p1.py)

### Explanation Part 1

Here we need to load each report as a list of integers (the levels).

Then we need to define two function that will hold the logic for a report to be "safe",
`is_decreasing` and `is_increasing`.

A report is considered safe if either one of the two functions returns True.

Then we just need to grab all the safe reports in a list and print it's length.

## Part 2

Solution file: [Part 2 solution](day2_p2.py)

### Explanation Part 2

For the second part, we need to modify the `is_decreasing`, `is_increasing`, and `is_report_safe` functions in order to add the logic for the "Problem Dampener".

This means that `is_report_safe` will check the bad indexes returned by `is_decreasing` and `is_increasing` and if one of them returns 0 bad indexes, the report is considered safe.
Otherwise it will attempt to remove one bad index at a time on the original report, checking if the report is safe after removing that single element, If no bad index removal turned the report safe, it is considered unsafe.

The solution is still the number of safe reports.
