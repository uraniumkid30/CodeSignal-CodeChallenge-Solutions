from ..matrix_element_sum import solution
import unittest


class TestAdjacentElementProduct(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [[1]]
        expected_result: int = 1
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [[4, 0, 1], [10, 7, 0], [0, 0, 0], [9, 1, 2]]
        expected_result: int = 15
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [[2], [5], [10]]
        expected_result: int = 17
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [[1], [5], [0], [2]]
        expected_result: int = 6
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        expected_result: int = 18
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
