"""
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
solution(n) = 0;
For n = 100, the output should be
solution(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
solution(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
5 ≤ n ≤ 109.

[output] integer
"""


def sort_return(number: str) -> str:
    return str(sum(list(map(int, number))))


def solution(n: int) -> int:
    number = str(n)
    result = 0
    while True:
        if (lambda x: True if len(x) < 2 else False)(number):
            break
        else:
            number = sort_return(number)
            result += 1
    return result
