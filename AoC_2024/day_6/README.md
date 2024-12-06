# AoC 2024 [Day 6](https://adventofcode.com/2024/day/6)

## Part 1

Solution file: [Part 1 solution](day6_p1.py)

### Explanation Part 1

The code reads a map from the input file, where symbols represent free cells, obstacles, and the player's starting position and direction.
It identifies the player's initial position and facing direction.
The player moves step-by-step in the grid, marking visited cells as X.
If the player encounters an obstacle or the map's edge, they turn clockwise and continue moving.
The program counts and prints the total number of visited cells marked as X.

## Part 2

Solution file: [Part 2 solution](day6_p2.py)

### Explanation Part 2

In this part, we need to find how many loops we can create by adding one single obstacle in the map.
I revisited some pieces of code from part one, but I eventually gave up in trying to figure out a
solution to detect an infinite loop. So i basically decided to give the function a timeout in order to detect infinite loops.
The code is really slow in finding the solution, don't try this at home! :P
