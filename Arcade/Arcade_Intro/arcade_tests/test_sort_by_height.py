from ..sort_by_height import solution
import unittest


class TestAdjacentElementProduct(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [-1, 150, 190, 170, -1, -1, 160, 180]
        expected_result: list = [-1, 150, 160, 170, -1, -1, 180, 190]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [-1]
        expected_result: list = [-1]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [4, 2, 9, 11, 2, 16]
        expected_result: list = [2, 2, 4, 9, 11, 16]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
        expected_result: list = [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
        expected_result: list = [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
