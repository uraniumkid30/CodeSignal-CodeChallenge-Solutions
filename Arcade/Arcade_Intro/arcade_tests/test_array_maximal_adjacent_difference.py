from ..array_maximal_difference import solution
import unittest


class TestArrayMaximalAdjacentDifference(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [2, 4, 1, 0]
        expected_result: int = 3
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [1, 1, 1, 1]
        expected_result: int = 0
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [-1, 4, 10, 3, -2]
        expected_result: int = 7
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [10, 11, 13]
        expected_result: int = 2
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [-1, 1, -3, -4]
        expected_result: int = 4
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
