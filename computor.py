#!/usr/bin/python3
import sys

from help.colors import BLUE, GREEN, MAGENTA, MANDATORY, RED, RESET, YELLOW
from help.tools import (get_degree_factor_pairs, get_flip_sign,
                        get_raw_equation, parse_fractions, pre_process,
                        print_solutions, solve_equation, validate_equation)

print(f"{MAGENTA}Welcome to the ComputorV1!{RESET}")

if len(sys.argv) != 2:
    print(f"{RED}Usage: ./computor.py <equation>{RESET}")
    sys.exit(1)

equation = sys.argv[1].replace(" ", "").split("=")

print(f"{MAGENTA}Step 1: Remove all spaces{RESET}")
print(f"{MAGENTA}Step 2: Move evrything to one side and flip the sign{RESET}")

if len(equation) != 2:
    print(f"{RED}The equation must contain one '='{RESET}")
    sys.exit(1)

if not validate_equation(equation):
    print(f"{RED}Invalid equation{RESET}")
    sys.exit(1)

equation = equation[0] + get_flip_sign(equation[1])

print(f"{BLUE}Equation:{YELLOW} {equation} = 0{MANDATORY}")

print(f"{MAGENTA}Step 3: Pre-process the equation{RESET}")

pre_processed = pre_process(equation)

print(f"{BLUE}Pre-processed:{YELLOW} {pre_processed}{MANDATORY}")

print(f"{MAGENTA}Step 4: Get factor of each degree{RESET}")
degree_factor = get_degree_factor_pairs(pre_processed)

print(f"{BLUE}Degree-Factor pairs:{YELLOW} {degree_factor}{MANDATORY}")


if len(degree_factor) == 0:
    # 0 = 0 or X = X, etc...
    print(f"{GREEN}All real numbers are solutions{RESET}")
    sys.exit(0)

max_degree = degree_factor[0][0]

if max_degree == 0:
    print(f"{RED}The equation is not solvable{RESET}")  # 1 = 2
    sys.exit(0)

raw_equation = get_raw_equation(degree_factor)

print(f"{BLUE}Reduced form:{YELLOW} {raw_equation}{RESET}")

print(f"{BLUE}Polynomial degree:{YELLOW} {max_degree}{MANDATORY}")

print(f"{MAGENTA}Step 5: Solve the equation{RESET}")

try:
    solutions = solve_equation(degree_factor, max_degree)
except ValueError as err:
    print(f"{RED}{err}{RESET}")
    sys.exit(0)

parse_fractions(solutions)
print_solutions(solutions)