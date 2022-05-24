"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer
"""
from .utils import timefunc
from collections import Counter


@timefunc("Common Character Count")
def solution(s1: str, s2: str) -> int:
    s1_count: Counter = Counter(s1)
    s2_count: Counter = Counter(s2)
    intersect: set = set(s1_count.keys()) & set(s2_count.keys())
    return sum(
        [
            min(s1_count.get(x), s2_count.get(x))
            for x in intersect
            if (s1_count.get(x) and s2_count.get(x))
        ]
    )
