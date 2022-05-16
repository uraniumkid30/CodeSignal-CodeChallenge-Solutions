"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
solution(st) = "abcdcba".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string st

A string consisting of lowercase English letters.

Guaranteed constraints:
3 ≤ st.length ≤ 10.

[output] string
"""


def solution(st: str) -> str:
    str_length: int = len(st)
    for i in range(str_length):
        sub_string = st[i:str_length]
        if sub_string[::-1] == sub_string:  # is palindrome?
            missing = st[0:i]
            return st + missing[::-1]
    return st
