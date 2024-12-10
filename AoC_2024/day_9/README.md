# AoC 2024 [Day 9](https://adventofcode.com/2024/day/9)

## Part 1

Solution file: [Part 1 solution](day9_p1.py)

### Explanation Part 1

After reading the input string, we convert it to long form, then we move the right most files into the leftmost spaces.
At last we calculate the checksum and get our solution.

## Part 2

Solution file: [Part 2 solution](day9_p2.py)

### Explanation Part 2

Here I modified the function to deal with list of integers instead, I store the files and gaps into separate lists, along with their start position.
Then I apply the rearrange logic to gather a list of compacted files along with their position.

The solution will still be the checksum.
