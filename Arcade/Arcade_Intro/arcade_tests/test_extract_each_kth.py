from ..extract_each_kth import solution
import unittest


class TestExtractEachKth(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k_value: int = 3
        expected_result: list = [1, 2, 4, 5, 7, 8, 10]
        result = solution(inputArray,k_value)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [1, 1, 1, 1, 1]
        k_value: int = 1
        expected_result: list = []
        result = solution(inputArray,k_value)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [1, 2, 1, 2, 1, 2, 1, 2]
        k_value: int = 2
        expected_result: list = [1, 1, 1, 1]
        result = solution(inputArray,k_value)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [1, 2, 1, 2, 1, 2, 1, 2]
        k_value: int = 10
        expected_result: list = [1, 2, 1, 2, 1, 2, 1, 2]
        result = solution(inputArray,k_value)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [2, 4, 6, 8, 10]
        k_value: int = 2
        expected_result: list = [2, 6, 10]
        result = solution(inputArray,k_value)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
