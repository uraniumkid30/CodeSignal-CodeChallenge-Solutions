from ..array_change import solution
import unittest


class TestArrayChange(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [1, 1, 1]
        expected_result: int = 3
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [-1000, 0, -2, 0]
        expected_result: int = 5
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [2, 1, 10, 1]
        expected_result: int = 12
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]
        expected_result: int = 13
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [3122, -645, 2616, 13213, -8069]
        expected_result: int = 25559
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
