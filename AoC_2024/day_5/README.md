# AoC 2024 [Day 5](https://adventofcode.com/2024/day/5)

## Part 1

Solution file: [Part 1 solution](day5_p1.py)

### Explanation Part 1

First I read the input file, parsing the updates into a list of integers, and the rules into a dictionary, which will hold the X values as keys with their corresponding Y values in a set.
After that i define a function that will scan an update array to see if it follows the rules.

This means iterating over the array one time, then for each position, if the number is in the rules keys, iterate again over the array, until the number position, effectively discarding numbers in front of it, and check if the current Y number is in the rules for X, if it is, since it's effectively behind, it breaks the rule.

After gathering the correct updates, we just grab the middle elements and sum them togheter to obtain the puzzle solution.

## Part 2

Solution file: [Part 2 solution](day5_p2.py)

### Explanation Part 2

Here we need to use the same function for checking if an update is correct, but instead gather all the uncorrect updates and fix them using the function `fix_update` which performs the Kahn's Algorithm topological sort.

The solution is the sum of middle values in the fixed updates.
