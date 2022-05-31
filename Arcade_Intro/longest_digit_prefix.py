"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
3 ≤ inputString.length ≤ 100.

[output] string
"""

import re
from .utils import time_solution


@time_solution(module_name="Longest digit Prefix")
def solution(inputString: str) -> str:
    pattern: str = "\d+"
    match_result = re.match(pattern, inputString)
    return match_result.group() if match_result else ""
