# AoC 2024 [Day 10](https://adventofcode.com/2024/day/10)

## Part 1

Solution file: [Part 1 solution](day10_p1.py)

### Explanation Part 1

First I read the input map, converting it into an matrix of integers, where '.' is -1.
Then I collected all the trailheads positions in a list of tuples.
For each trailhead, the `get_trailhead_score` function calculates a score by traversing the map. It uses a stack to perform a [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search), looking for cells with incrementing values until it reaches a cell with a value of 9.
The scores from all trailheads are summed to get the solution.

## Part 2

Solution file: [Part 2 solution](day10_p2.py)

### Explanation Part 2

All I changed from part one script to solve part two was the `get_trailhead_score` becoming `get_trailhead_rating`, the new function works recursively. It starts at the given position and looks for nearby cells with a specific step value. If only one cell is found, it moves to that cell and increments the step value. If multiple cells are found, it recursively calculates the rating for each of those cells and adds them to the current rating. The recursion stops when the step value exceeds 9, and the rating is incremented by 1.

The solution is the sum af all ratings for all trailheads.
