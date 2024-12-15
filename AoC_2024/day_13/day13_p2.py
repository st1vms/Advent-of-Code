"""AoC 2024 Day 13 Part 1 solution"""

import re
from dataclasses import dataclass
from typing import List, Tuple, Dict, Union
from scipy.optimize import linprog

INPUT_FILE = "input.txt"

OFFSET = 10000000000000

@dataclass
class ClawMachineData:
    """Claw machine input data"""

    button_a: tuple[int]
    button_b: tuple[int]
    prize_loc: tuple[int]


def read_input(input_file: str) -> list[ClawMachineData]:
    """Reads the input file as a lit of ClawMachineData"""

    btn_pattern = r"Button [A-Z]: X\+(\d+), Y\+(\d+)"
    price_pattern = r"Prize: X=(\d+), Y=(\d+)"

    claws_data = []
    with open(input_file, "r", encoding="utf-8") as fp:
        claws_text = fp.read().strip().split("\n\n")
        for claw_text in claws_text:

            a_btn_line, b_btn_line, prize_loc_line = claw_text.split("\n")

            # Read buttons properties
            button_a = re.search(btn_pattern, a_btn_line)
            button_a = (int(button_a.group(1)), int(button_a.group(2)))
            button_b = re.search(btn_pattern, b_btn_line)
            button_b = (int(button_b.group(1)), int(button_b.group(2)))

            # Reads price location
            # Also add offset
            price_loc = re.search(price_pattern, prize_loc_line)
            price_loc = (int(price_loc.group(1)) + OFFSET, int(price_loc.group(2)) + OFFSET)

            claws_data.append(ClawMachineData(button_a, button_b, price_loc))

    return claws_data


def simplex_algorithm(
    num_variables: int,
    objective_coeffs: List[float],
    maximize: bool,
    constraints: List[Tuple[List[float], str, float]],
) -> Dict[str, Union[str, float, List[float]]]:
    """Performs the simplex algorithm to solve a linear programming problem."""

    # Ensure the dimensions of the problem match
    if len(objective_coeffs) != num_variables:
        raise ValueError(
            "The length of the objective coefficients must match the number of variables."
        )

    # Initialize lists for constraints matrix (A) and bounds vector (b)
    a: List[List[float]] = []  # Coefficients for the constraints
    b: List[float] = []  # Bounds for the constraints

    # Process each constraint
    for constraint in constraints:
        coeffs, inequality, bound = constraint
        if len(coeffs) != num_variables:
            raise ValueError(
                "Each constraint must have coefficients matching the number of variables."
            )

        if inequality == "<=":
            a.append(coeffs)
            b.append(bound)
        elif inequality == ">=":
            # Convert '>=' into '<=' by multiplying by -1
            a.append([-c for c in coeffs])
            b.append(-bound)
        elif inequality == "=":
            # For equality, split into two inequalities
            a.append(coeffs)
            b.append(bound)
            a.append([-c for c in coeffs])
            b.append(-bound)
        else:
            raise ValueError("Inequality must be either '<=', '>=', or '='.")

    # If maximizing, negate the objective function coefficients
    c: List[float] = [-x for x in objective_coeffs] if maximize else objective_coeffs

    # Variable bounds (assuming non-negative variables)
    bounds: List[Tuple[float, float]] = [
        (0, None)
    ] * num_variables  # Variables are non-negative by default

    # Solve using scipy's linprog method
    result = linprog(c, A_ub=a, b_ub=b, bounds=bounds, method="highs")

    # Check the result and return the outcome
    if result.success:
        return {
            "status": "success",
            "objective_value": result.fun if not maximize else -result.fun,
            "variable_values": result.x.tolist(),
        }
    return {"status": "failure", "message": result.message}


def calculate_tokens(claw: ClawMachineData) -> int:
    """Returns minimum amount of tokens to reach prize, 0 if it cannot be reached"""

    # Perfom simplex algorithm to minimize tokens by button presses
    res = simplex_algorithm(
        2,  # Two variables
        [3, 1],  # Price for each button press
        False,  # Minimize
        [
            # Constraints for the problem
            [[claw.button_a[0], claw.button_b[0]], "=", claw.prize_loc[0]],
            [[claw.button_a[1], claw.button_b[1]], "=", claw.prize_loc[1]],
        ],
    )
    if res["status"] == "failure":
        return 0

    # Check if solution meets constraints
    a_press, b_press = res["variable_values"]

    if claw.prize_loc[0] != (round(a_press) * claw.button_a[0]) + (
        round(b_press) * claw.button_b[0]
    ):
        return 0

    if claw.prize_loc[1] != (round(a_press) * claw.button_a[1]) + (
        round(b_press) * claw.button_b[1]
    ):
        return 0

    return round(res["objective_value"])


def _main() -> None:

    # Reads input
    claws = read_input(INPUT_FILE)

    # Finds solution
    min_tokens = sum(calculate_tokens(claw) for claw in claws)

    # Prints solution
    print(f"Min amount of tokens to spend: {min_tokens}")


if __name__ == "__main__":
    _main()
