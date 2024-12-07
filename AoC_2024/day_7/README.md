# AoC 2024 [Day 7](https://adventofcode.com/2024/day/7)

## Part 1

Solution file: [Part 1 solution](day7_p1.py)

### Explanation Part 1

We read the equations as a list of tuples, storing the result and the parameters inside another tuple.
Then we define a function that will calculate the cartesian product of the two operators (+ and *) and will try all possible combinations with the available parameters.
To get our solution we sum the result of all the equations that have at least one valid combination of paramters.

## Part 2

Solution file: [Part 2 solution](day7_p2.py)

### Explanation Part 2

Part 2 is pretty straightforward, we just need to add one more symbol to te `itertools.product` function and define the logic of "combination" for that new operator.
Solution is still the sum of all results that have valid combination.
