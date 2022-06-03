from ..adjacent_element_product import solution
import unittest


class TestAdjacentElementProduct(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [3, 6, -2, -5, 7, 3]
        expected_result: int = 21
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [-1, -2]
        expected_result: int = 2
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [5, 1, 2, 3, 1, 4]
        expected_result: int = 6
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [-23, 4, -3, 8, -12]
        expected_result: int = -12
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [5, 6, -4, 2, 3, 2, -23]
        expected_result: int = 30
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
