from ..alternating_sums import solution
import unittest


class TestAdjacentElementProduct(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [50, 60, 60, 45, 70]
        expected_result: list = [180, 105]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [100, 50, 50, 100]
        expected_result: list = [150, 150]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [100, 51, 50, 100]
        expected_result: list = [150, 151]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [80]
        expected_result: list = [80, 0]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [100, 50]
        expected_result: list = [100, 50]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
