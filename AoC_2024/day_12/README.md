# AoC 2024 [Day 12](https://adventofcode.com/2024/day/12)

## Part 1

Solution file: [Part 1 solution](day12_p1.py)

### Explanation Part 1

The `read_input` function reads the input map from a file (input.txt) and returns it as a list of strings, where each string represents a row of the map.
The `calculate_area_and_perimeter` function uses [Breadth-First Search (BFS)](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/) to explore each region of the map. It calculates the area (number of cells) and perimeter (number of boundary edges) of each region. The function keeps track of visited cells to avoid reprocessing.

The `calculate_total_price` function iterates over all cells in the grid. For each unvisited cell, it calls `calculate_area_and_perimeter` to get the area and perimeter of the region starting from that cell. It then calculates the price for fencing that region (area * perimeter) and adds it to the total price.

## Part 2

Solution file: [Part 2 solution](day12_p2.py)

### Explanation Part 2

The `read_input` function converts the input map into a dictionary with complex numbers as keys and characters as values.
The `neighbours` function returns neighbouring cells for a given cell.
The `region_neighbours` function finds neighbouring cells of a region with the same character.
The `regions` function groups unvisited cells into distinct regions.
The `perimeter` function counts boundary edges of a region.
The `corners` function determines the number of corners in a region for fencing cost.
The `_main` function reads input, calculates total price by summing the product of region size and corners, and prints the total price.
