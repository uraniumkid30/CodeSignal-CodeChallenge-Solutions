"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.
"""

import string


def solution(inputString: str) -> str:
    str_bank: str = string.ascii_lowercase
    bank: dict = dict(zip(str_bank, range(len(str_bank))))
    result = ""
    for item_no, item in enumerate(inputString):
        letter_reference: int = bank.get(item) + 1
        if letter_reference > 25:
            letter_reference = 0
        result += str_bank[letter_reference]
    return result
