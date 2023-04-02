from .explainations import print_linear_explaination, print_quadratic_explaination
from .colors import GREEN, RED, RESET, YELLOW
from .my_math import sqrt, abs


def validate_equation(equation: list[str]):
    import re
    equation_validator = re.compile(
        "(((^[+-]?)|[+-])(([0-9]+(\.[0-9]+)?(\*X(\^[0-9]+)?)?)|(([0-9]+(\.[0-9]+)?\*)?X(\^[0-9]+)?)))+$")
    return equation_validator.match(equation[0]) and equation_validator.match(equation[1])


def get_flip_sign(s: str):
    fliped = s.replace("-", "~").replace("+", "-").replace("~", "+")
    if fliped[0] not in ["+", "-"]:
        fliped = "-" + fliped
    return fliped


def pre_process(equation: str):
    pre_process = []
    curr = ""
    for i in equation:
        if i == "+" or i == "-":
            curr and pre_process.append(curr)
            curr = i
        else:
            curr += i
    curr and pre_process.append(curr)
    return pre_process


def get_degree_factor_pairs(pre_processed: list[str]):
    degree_factor = {}
    for i in pre_processed:
        factor = None
        degree = None
        x_part = None
        if "*" in i:
            factor = round(float(i.split("*")[0]), 2)
            x_part = i.split("*")[1]
        elif "X" not in i:
            factor = round(float(i), 2)
            x_part = ""
        else:
            factor = -1 if i[0] == '-' else 1
            x_part = i

        if "^" in x_part:
            degree = int(x_part.split("^")[1])
        elif "X" in x_part:
            degree = 1
        else:
            degree = 0

        degree_factor[degree] = round(degree_factor.get(degree, 0) + factor, 2)

    sorted_result = sorted(degree_factor.items(),
                           key=lambda x: x[0], reverse=True)
    filtered_result = filter(lambda x: x[1] != 0, sorted_result)

    return list(filtered_result)


def get_raw_equation(equation: list[tuple[int, float]]):
    raw_equation_parts = []

    for term in equation:
        degree, factor = map(int_or_float, term)
        sign = '-' if factor < 0 else '+'

        if len(raw_equation_parts) == 0 and sign == '-':
            raw_equation_parts.append(sign)
        elif len(raw_equation_parts) != 0:
            raw_equation_parts.append(f" {sign} ")

        if degree == 0:
            raw_equation_parts.append(f"{abs(factor)}")
        elif degree == 1 and abs(factor) == 1:
            raw_equation_parts.append("X")
        elif degree == 1:
            raw_equation_parts.append(f"{abs(factor)}X")
        else:
            raw_equation_parts.append(f"{abs(factor)}X^{degree}")
    raw_equation_str = "".join(raw_equation_parts) + " = 0"
    return raw_equation_str


def int_or_float(number):
    return int(number) if int(number) == number else round(number, 6)


def solve_linear(equation: dict[int, float]):
    ret = {}
    a = equation.get(1, 0)
    b = equation.get(0, 0)

    print_linear_explaination(a, b)

    if a == 0:
        raise ValueError("Cannot solve linear equation with a = 0")

    ret["solutions"] = (int_or_float(-b / a),)
    ret["number_of_solutions"] = 1
    ret["solutions_as_fractions"] = ((-b, a),)
    ret["delta"] = None
    return ret


def solve_quadratic(equation: dict[int, float]):
    ret = {}
    a = equation.get(2, 0)
    b = equation.get(1, 0)
    c = equation.get(0, 0)

    delta = round(b * b - 4 * a * c, 2)
    ret["delta"] = delta

    print_quadratic_explaination(a, b, c, delta)

    if delta < 0:
        ret["solutions"] = None
        ret["number_of_solutions"] = 0
        ret["solutions_as_fractions"] = None
        return ret

    if delta == 0:
        ret["solutions"] = (int_or_float(-b / (2 * a)),)
        ret["number_of_solutions"] = 1
        ret["solutions_as_fractions"] = ((-b, 2 * a),)
        return ret

    sqrt_delta = sqrt(delta)
    ret["solutions"] = (int_or_float((-b - sqrt_delta) / (2 * a)),
                        int_or_float((-b + sqrt_delta) / (2 * a)))
    ret["number_of_solutions"] = 2
    ret["solutions_as_fractions"] = (
        (-b - sqrt_delta, 2 * a), (-b + sqrt_delta, 2 * a))
    return ret


def solve_equation(equation: list[tuple[int, float]], degree: int):
    equation_as_dict = {key: value for key, value in equation}

    if degree > 2:
        raise ValueError(
            "The polynomial degree is stricly greater than 2, I can't solve.")

    if degree == 1:
        return solve_linear(equation_as_dict)

    return solve_quadratic(equation_as_dict)


def print_solutions(solutions: dict[str, any]):
    if solutions["number_of_solutions"] == 0:
        print(f"{RED}The equation has no real solutions.{RESET}")
        return

    if solutions["number_of_solutions"] == 1:
        solution = solutions["solutions"][0]
        solution_as_fraction = solutions["solutions_as_fractions"][0]
        print(
            f"{GREEN}The solution is: {YELLOW}{solution}{RESET} {solution_as_fraction}{RESET}")
        return

    solution1 = solutions["solutions"][0]
    solution2 = solutions["solutions"][1]
    solution1_as_fraction = solutions["solutions_as_fractions"][0]
    solution2_as_fraction = solutions["solutions_as_fractions"][1]

    print(f"{GREEN}The solutions are: {YELLOW}{solution1}{RESET} {solution1_as_fraction}{RESET}")
    print(f"{GREEN}and {YELLOW}{solution2}{RESET} {solution2_as_fraction}{RESET}")


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def parse_fractions(solutions: dict[str, any]):
    if solutions["number_of_solutions"] == 0:
        return

    as_strings = []

    for a, b in solutions["solutions_as_fractions"]:
        aa = int(a // gcd(a, b))
        bb = int(b // gcd(a, b))
        sign = -1 if aa * bb < 0 else 1
        fraction = ""
        if abs(bb) != 1 and aa < 100 and bb < 100:
            fraction = f"{GREEN}or {YELLOW}{abs(aa) * sign}/{abs(bb)}"
        as_strings.append(fraction)

    solutions["solutions_as_fractions"] = tuple(as_strings)
