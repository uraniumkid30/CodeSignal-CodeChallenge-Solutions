"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-105 ≤ inputArray[i] ≤ 105.

[output] integer

The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.
"""
from .utils import timefunc


@timefunc("Array Change")
def solution(inputArray: list) -> int:
    number_of_moves: int = 0
    first_item = inputArray[0]
    for item in inputArray[1:]:
        if item <= first_item:
            number_of_moves += first_item - item + 1
            first_item += 1
        else:
            first_item = item
    return number_of_moves
