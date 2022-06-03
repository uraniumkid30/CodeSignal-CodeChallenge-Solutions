"""
Find the leftmost digit that occurs in a given string.

Example

For inputString = "var_1__Int", the output should be
solution(inputString) = '1';
For inputString = "q2q-q", the output should be
solution(inputString) = '2';
For inputString = "0ss", the output should be
solution(inputString) = '0'.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string containing at least one digit.

Guaranteed constraints:
3 ≤ inputString.length ≤ 10.

[output] char
"""
from .utils import time_solution


@time_solution(module_name="First Digit")
def solution(inputString: list) -> str:
    for x in inputString:
        if x.isdigit():
            return x
