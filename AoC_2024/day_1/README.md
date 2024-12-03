# AoC 2024 [Day 1](https://adventofcode.com/2024/day/1)

## Part 1

Solution file: [Part 1 solution](day1_p1.py)

### Explanation Part 1

Here we're dealing with two lists of numbers that have the same size.

We first need to read the two lists in the file, then we need to sort them out, and loop through each element using zip.

This way we can grab the distances from the lowest numbers to the highest ones, sum them togheter and get our solution.

## Part 2

Solution file: [Part 2 solution](day1_p2.py)

### Explanation Part 2

In the second part, we're dealing with the same input list, so the reading part is the same.

This time we simply have to loop through one list and count the occurrences of the item in the second list, saving the score as the multiplication of the count with the item.

The solution will be the sum of all saved scores.
