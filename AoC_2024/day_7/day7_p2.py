"""AoC 2024 Day 7 Part 2 solution"""

from itertools import product

INPUT_FILE = "input.txt"


def read_equations(input_file: str) -> list[tuple[int, tuple[int]]]:
    """Read input file and return list of equations"""
    eqs = []
    with open(input_file, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            ret, params_line = line.strip().split(":")
            params = [int(i) for i in filter(bool, params_line.split(" "))]
            eqs.append((int(ret), (*params,)))
    return eqs


def find_operators(res: int, params: list[int]) -> list[tuple[str]]:
    """Given a result number and the possible param,eters,
    return a list of tuples with the operators ('+', '*' and '|') that fulfill the equation,
    an empty list if no operators were found."""

    # Need at least two numbers to apply operators
    if len(params) < 2:
        return []

    # Generate all possible combinations of '+' and '*'
    operator_combinations = product("+*|", repeat=len(params) - 1)
    valid_op_combinations = []

    for operators in operator_combinations:
        total = params[0]
        for op, num in zip(operators, params[1:]):
            if op == "+":
                total += num
            elif op == "*":
                total *= num
            elif op == "|":
                total = int(str(total) + str(num))

        # Check if the current combination yields the desired result
        if total == res:
            valid_op_combinations.append(operators)

    return valid_op_combinations


def _main() -> None:
    equations = read_equations(INPUT_FILE)

    # Finds solution
    calib_res = 0
    for eq in equations:
        res, params = eq
        if find_operators(res, params):
            calib_res += res

    # Prints solution
    print(f"Total calibration result: {calib_res}")


if __name__ == "__main__":
    _main()
