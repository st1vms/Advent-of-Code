# AoC 2024 [Day 4](https://adventofcode.com/2024/day/4)

## Part 1

Solution file: [Part 1 solution](day4_p1.py)

### Explanation Part 1

In this puzzle, we need to look inside a character matrix for all the occurrences of the word 'XMAS'.
To do so we define a function that based off a starting x,y position, gets us all neighbour cells around.
Then we iterate over each position in the input matrix, considering only the ones that starts with the first letter of 'XMAS',
and look for the presence of the remaining string in the corresponding direction, incrementig the total when the word is found.

The solution will the total number of occurrences of 'XMAS' in the input matrix.

## Part 2

Solution file: [Part 2 solution](day4_p2.py)

### Explanation Part 2

In order to find all X-MAS combinations, we need to edit the functions, in order to return only diagonal neigbours, and with only one cell for each diagonal.

Then I implemented a simple logic to check if a three letter word like 'MAS' is present in X combination inside a matrix.
