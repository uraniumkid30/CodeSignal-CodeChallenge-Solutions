"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of digits, full stops and lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 30.

[output] boolean

true if inputString satisfies the IPv4 address naming rules, false otherwise.

"""
from .utils import time_solution


@time_solution(module_name="Is IPV4 Address")
def solution(inputString: str) -> bool:
    ip_number = inputString.split(".")
    if len(ip_number) != 4:
        return False
    for number in ip_number:
        if not number.isdigit():
            return False
        if len(number) != 1 and number[0] == "0":
            return False
        if not (0 <= int(number) <= 255):
            return False
    return True
