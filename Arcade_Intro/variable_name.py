"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
solution(name) = true;
For name = "qq-q", the output should be
solution(name) = false;
For name = "2w2", the output should be
solution(name) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string name

Guaranteed constraints:
1 ≤ name.length ≤ 10.

[output] boolean

true if name is a correct variable name, false otherwise.
"""

import re

from .utils import time_solution


@time_solution(module_name="Variable Name")
def solution(name):
    pattern = r"^[a-z,A-Z,_][0-9a-z,A-Z,_]*$"
    return True if re.match(pattern, name) else False
