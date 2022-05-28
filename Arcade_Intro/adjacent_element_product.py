"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.


"""

from typing import Union
from .utils import time_solution


@time_solution("Adjacent Element Product")
def solution(inputArray: Union[tuple, list]) -> int:
    # create a generator using a zipper
    paired_list = (pair[0] * pair[1] for pair in zip(inputArray[:-1], inputArray[1:]))
    return max(paired_list)
