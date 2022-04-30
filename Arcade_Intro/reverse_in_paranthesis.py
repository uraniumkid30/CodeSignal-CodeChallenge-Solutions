"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters and the characters ( and ). It is guaranteed that all parentheses in inputString form a regular bracket sequence.

Guaranteed constraints:
0 ≤ inputString.length ≤ 50.

[output] string

Return inputString, with all the characters that were in parentheses reversed.
"""


def solution(inputString: str) -> str:
    s = inputString
    chars: list = list(s)
    open_bracket_indexes: list = []
    for i, c in enumerate(chars):
        if c == "(":
            open_bracket_indexes.append(i)
        elif c == ")":
            j = open_bracket_indexes.pop()
            chars[j:i] = chars[i:j:-1]
    if open_bracket_indexes:
        raise ArgumentError("Unclosed parenthesis")
    return "".join(c for c in chars if c not in "()")
