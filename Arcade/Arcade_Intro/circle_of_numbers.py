"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
solution(n, firstNumber) = 7.



Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive even integer.

Guaranteed constraints:
4 ≤ n ≤ 20.

[input] integer firstNumber

Guaranteed constraints:
0 ≤ firstNumber ≤ n - 1.

[output] integer
"""
from .utils import time_solution


@time_solution(module_name="Circle Of Numbers")
def solution(total_number: int, firstNumber: int) -> int:
    mid = total_number / 2
    result: int = firstNumber + mid
    if firstNumber > mid:
        result = firstNumber - mid
    elif firstNumber == mid:
        result = 0
    return result
