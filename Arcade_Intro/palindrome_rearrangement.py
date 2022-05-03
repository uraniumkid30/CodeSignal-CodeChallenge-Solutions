"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
"""

from collections import Counter


def solution(inputString: str) -> bool:
    item_frequency: Counter = Counter(inputString)
    odd_no_count: int = 0
    for i in item_frequency.values():
        if i % 2 == 1:
            odd_no_count += 1
        if odd_no_count > 1:
            return False

    return True
