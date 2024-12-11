# AoC 2024 [Day 11](https://adventofcode.com/2024/day/11)

## Part 1

Solution file: [Part 1 solution](day11_p1.py)

### Explanation Part 1

The solution to part one is pretty easy, I just read the stones as a list of strings.
Then I apply the blink logic N times to get the new stones, and print the solution which will be total amount of new stones after blinking.

## Part 2

Solution file: [Part 2 solution](day11_p2.py)

### Explanation Part 2

Part two is trickier, we can't use the same function as part one, as it will result in a MemoryError.
Instead we can define a better approach using a Counter, that smartly track the amount of stones for each blink.
The solution becomes pretty fast with this method.
