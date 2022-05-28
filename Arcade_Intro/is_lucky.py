"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
"""
from .utils import time_solution


@time_solution("Is Lucky")
def solution(n: int) -> bool:
    num_list = list(str(n))
    mid_point: int = len(num_list) // 2
    first_half: int = sum(map(int, num_list[:mid_point]))
    last_half: int = sum(map(int, num_list[mid_point:]))
    return first_half == last_half
