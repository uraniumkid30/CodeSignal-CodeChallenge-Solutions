from ..box_blur import solution
import unittest


class TestBoxBlur(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [[1, 1, 1], [1, 7, 1], [1, 1, 1]]
        expected_result: list = [[1]]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [[0, 18, 9], [27, 9, 0], [81, 63, 45]]
        expected_result: list = [[28]]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [[36, 0, 18, 9], [27, 54, 9, 0], [81, 63, 72, 45]]
        expected_result: list = [[40, 30]]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [[7, 4, 0, 1], [5, 6, 2, 2], [6, 10, 7, 8], [1, 4, 2, 0]]
        expected_result: list = [[5, 4], [4, 4]]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [
            [36, 0, 18, 9, 9, 45, 27],
            [27, 0, 54, 9, 0, 63, 90],
            [81, 63, 72, 45, 18, 27, 0],
            [0, 0, 9, 81, 27, 18, 45],
            [45, 45, 27, 27, 90, 81, 72],
            [45, 18, 9, 0, 9, 18, 45],
            [27, 81, 36, 63, 63, 72, 81],
        ]
        expected_result: list = [
            [39, 30, 26, 25, 31],
            [34, 37, 35, 32, 32],
            [38, 41, 44, 46, 42],
            [22, 24, 31, 39, 45],
            [37, 34, 36, 47, 59],
        ]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
