"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.



For cell1 = "A1" and cell2 = "H3", the output should be
solution(cell1, cell2) = false.



Input/Output

[execution time limit] 4 seconds (py3)

[input] string cell1

Guaranteed constraints:
cell1.length = 2,
'A' ≤ cell1[0] ≤ 'H',
1 ≤ cell1[1] ≤ 8.

[input] string cell2

Guaranteed constraints:
cell2.length = 2,
'A' ≤ cell2[0] ≤ 'H',
1 ≤ cell2[1] ≤ 8.

[output] boolean

true if both cells have the same color, false otherwise.
"""


def solution(cell1: str, cell2: str) -> bool:
    board_letters: str = "ABCDEFGH"
    bank: dict = dict(zip(board_letters, range(1, len(board_letters) + 1)))
    even = lambda x: 0 if int(x) % 2 == 0 else 1
    cell1l_bool: int = even(bank.get(cell1[0]))
    cell2l_bool: int = even(bank.get(cell2[0]))
    cell1n_bool: int = even(cell1[1])
    cell2n_bool: int = even(cell2[1])
    cell1r = cell1l_bool + cell1n_bool
    cell2r = cell2l_bool + cell2n_bool
    return even(cell1r) == even(cell2r)
