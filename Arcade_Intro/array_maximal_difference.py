"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 10,
-15 ≤ inputArray[i] ≤ 15.

[output] integer

The maximal absolute difference.
"""


def solution(inputArray: list) -> int:
    for item in range(len(inputArray)):
        if item == 0:
            result = 0
        elif abs(inputArray[item] - inputArray[item - 1]) >= result:
            result = abs(inputArray[item] - inputArray[item - 1])
    return result
