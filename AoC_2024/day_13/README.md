# AoC 2024 [Day 13](https://adventofcode.com/2024/day/13)

## Part 1

Solution file: [Part 1 solution](day13_p1.py)

### Explanation Part 1

To solve this puzzle, we can use the Simplex Algorithm to solve the minimization problem of 3x1 + x2. With x1 and x2 being the amount of buttons presses for A and B, multiplied by their token amount.
For each claw we have a problem with two constraints that imply A\*x1 + B\*x2 = Prize Location X/Y.
Using this method we can easily calculate the minimum amount of tokens needed to reach the prize location.

## Part 2

Solution file: [Part 2 solution](day13_p2.py)

### Explanation Part 2

Part two uses the same script as part one, but adds an offset of `10000000000000` to the price location X/Y coordinates.
