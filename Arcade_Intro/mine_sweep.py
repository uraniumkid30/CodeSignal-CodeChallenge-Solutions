"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

solution(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
Check out the image below for better understanding:



Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.boolean matrix

A non-empty rectangular matrix consisting of boolean values - true if the corresponding cell contains a mine, false otherwise.

Guaranteed constraints:
2 ≤ matrix.length ≤ 100,
2 ≤ matrix[0].length ≤ 100.

[output] array.array.integer

Rectangular matrix of the same size as matrix each cell of which contains an integer equal to the number of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.
"""


def solution(matrix: list) -> list:
    number_of_rows: int = len(matrix)
    number_of_columns: int = len(matrix[0])
    result = [[0 for i in range(number_of_columns)] for j in range(number_of_rows)]
    dummy_matrix = [
        [0 for i in range(number_of_columns + 2)] for j in range(number_of_rows + 2)
    ]

    for i in range(number_of_rows):
        for j in range(number_of_columns):
            dummy_matrix[i + 1][j + 1] = matrix[i][j]

    for x in range(number_of_rows):
        for y in range(number_of_columns):
            result[x][y] = (
                dummy_matrix[x][y]
                + dummy_matrix[x][y + 1]
                + dummy_matrix[x][y + 2]
                + dummy_matrix[x + 1][y]
                + dummy_matrix[x + 1][y + 2]
                + dummy_matrix[x + 2][y]
                + dummy_matrix[x + 2][y + 1]
                + dummy_matrix[x + 2][y + 2]
            )
    return result
