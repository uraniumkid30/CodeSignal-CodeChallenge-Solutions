"""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 109.

[output] boolean

true if all digits of n are even, false otherwise.
"""


def solution(num: int) -> bool:
    for item in str(num):
        x: int = int(item)
        if x == 0:
            continue
        try:
            rem = x % 2
            if rem != 0:
                return False
        except Exception as err:
            return False
    else:
        return True
