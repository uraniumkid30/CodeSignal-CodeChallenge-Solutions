"""
    Given the string, check if it is a palindrome.

    Example

    For inputString = "aabaa", the output should be
    solution(inputString) = true;
    For inputString = "abac", the output should be
    solution(inputString) = false;
    For inputString = "a", the output should be
    solution(inputString) = true.
    Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    A non-empty string consisting of lowercase characters.

    Guaranteed constraints:
    1 ≤ inputString.length ≤ 105.

    [output] boolean

    true if inputString is a palindrome, false otherwise.
"""

from typing import Union


def solution(inputValue: Union[int, str]) -> bool:
    return str(inputValue) == str(inputValue)[::-1]


def solution(inputValue: Union[int, str]) -> bool:
    reversed_input: str = "".join(reversed(str(inputValue)))
    return str(inputValue) == reversed_input
