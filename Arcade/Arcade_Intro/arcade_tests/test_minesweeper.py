from ..mine_sweep import solution
import unittest


class TestMinesweeper(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [
            [True, False, False],
            [False, True, False],
            [False, False, False],
        ]
        expected_result: list = [[1, 2, 1], [2, 1, 1], [1, 1, 1]]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [[False, False, False], [False, False, False]]
        expected_result: list = [[0, 0, 0], [0, 0, 0]]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [
            [True, False, False, True],
            [False, False, True, False],
            [True, True, False, True],
        ]
        expected_result: list = [[0, 2, 2, 1], [3, 4, 3, 3], [1, 2, 3, 1]]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [[True, True, True], [True, True, True], [True, True, True]]
        expected_result: list = [[3, 5, 3], [5, 8, 5], [3, 5, 3]]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [
            [True, False],
            [True, False],
            [False, True],
            [False, False],
            [False, False],
        ]
        expected_result: list = [[1, 2], [2, 3], [2, 1], [1, 1], [0, 0]]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
