
from .colors import CYAN, GREEN, RED, RESET, YELLOW

QUADRATIC = f"""
{CYAN}The solution is: {YELLOW}-b ± sqrt(delta) / 2a{RESET}
{CYAN}with {YELLOW}a{CYAN} the coefficient of X^2, which is {YELLOW}{{}}{RESET}
{YELLOW}b{CYAN} the coefficient of X, which is {YELLOW}{{}}{RESET}
{CYAN}and {YELLOW}c{CYAN} the constant, which is {YELLOW}{{}}{RESET}
{CYAN}The discriminant is {YELLOW}delta = b² - 4ac{RESET}
{CYAN}which is {YELLOW}{{}}{RESET}

{CYAN}if delta{YELLOW} is {RED}negative{YELLOW}, there are {RED}no solutions{RESET}
{CYAN}if delta{YELLOW} is {GREEN}zero{YELLOW}, there is {GREEN}one solution{RESET}
{CYAN}if delta{YELLOW} is {CYAN}positive{YELLOW}, there are {CYAN}two solutions{RESET}
"""

LINEAR = f"""
{CYAN}The solution is: {YELLOW}-b / a{RESET}
{CYAN}with {YELLOW}a{CYAN} the coefficient of X, which is {YELLOW}{{}}{RESET}
{CYAN}and {YELLOW}b{CYAN} the constant, which is {YELLOW}{{}}{RESET}

{CYAN}if {YELLOW}a{CYAN} is {RED}zero{YELLOW}, there are {RED}no solutions{RESET}
"""

def print_quadratic_explaination(a: int, b: int, c: int, delta: int):
    print(QUADRATIC.format(a, b, c, delta))

def print_linear_explaination(a: int, b: int):
    print(LINEAR.format(a, b))

