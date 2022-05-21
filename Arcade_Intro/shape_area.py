"""
Below we will define an n-interesting polygon.
Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side.

Example

For n = 2, the output should be
solution(n) = 5;
For n = 3, the output should be
solution(n) = 13.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n < 104.

[output] integer

The area of the n-interesting polygon.
"""
from .utils import timefunc


@timefunc("Shape Area")
def solution(polygon_number: int) -> int:
    term_a = 2 * (polygon_number ** 2)
    term_b = 2 * polygon_number
    term_c = term_a - term_b
    result = term_c + 1
    return result
