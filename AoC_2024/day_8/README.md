# AoC 2024 [Day 8](https://adventofcode.com/2024/day/8)

## Part 1

Solution file: [Part 1 solution](day8_p1.py)

### Explanation Part 1

After reading the input matrix, I get the antennas positions inside a dictionary, that will hold antennas symbols as keys with their positions as values.
Then I use `itertools.combinations` to produce all the possible pairs of coordinates, and for each pair I calculate the two antinode coordinates, check if they are out of bounds, or can be placed, if so I return them.

The solution will be the length of the antinode positions list.

## Part 2

Solution file: [Part 2 solution](day8_p2.py)

### Explanation Part 2

To complete part 2 we had to calculate more antinodes, based off the dimension of the map.
And also we have to consider the antennas that have at least two similar ones on the map, as antinodes. discarding the ones that were previously counted as overlapping antinodes.

The solution is still the length of the antinode positions list.
