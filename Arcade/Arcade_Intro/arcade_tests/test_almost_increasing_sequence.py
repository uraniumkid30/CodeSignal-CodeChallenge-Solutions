from ..almost_increasing_sequence import solution
import unittest


class TestAdjacentElementProduct(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [3, 5, 67, 98, 3]
        expected_result: bool = True
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [40, 50, 60, 10, 20, 30]
        expected_result: bool = False
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [10, 1, 2, 3, 4, 5, 6, 1]
        expected_result: bool = False
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [10, 1, 2, 3, 4, 5]
        expected_result: bool = True
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [123, -17, -5, 1, 2, 3, 12, 43, 45]
        expected_result: bool = True
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
