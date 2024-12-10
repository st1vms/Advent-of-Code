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
