# AoC 2024 [Day 3](https://adventofcode.com/2024/day/3)

## Part 1

Solution file: [Part 1 solution](day3_p1.py)

### Explanation Part 1

In order to find all the valid multiplication instructions, we need to construct a regex pattern,
this pattern will do the trick `r"mul\((\d+),(\d+)\)"`.
Once all instructions are gathered, the solution can be easily calculated.

## Part 2

Solution file: [Part 2 solution](day3_p2.py)

### Explanation Part 2

Here we need to edit our regex in order to match multiple groups, so that we can gather all the instructions.
This regex is what worked for me:

`r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"` .

After gathering all the instructions, we loop through them, enabling or disabling the next multiplication instruction in case a do() or don't() is found.
