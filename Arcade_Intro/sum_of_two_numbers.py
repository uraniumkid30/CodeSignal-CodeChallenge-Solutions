# Qestion
"""
    Write a function that returns the sum of two numbers.

    Example

    For param1 = 1 and param2 = 2, the output should be
    solution(param1, param2) = 3.

    Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer param1

    Guaranteed constraints:
    -1000 ≤ param1 ≤ 1000.

    [input] integer param2

    Guaranteed constraints:
    -1000 ≤ param2 ≤ 1000.

    [output] integer

    The sum of the two inputs.
"""

# Solution

from typing import Union
from .utils import time_solution


@time_solution(module_name="Sum Of Two Numbers")
def solution(param1: Union[int, float], param2: Union[int, float]) -> Union[int, float]:
    return param1 + param2
