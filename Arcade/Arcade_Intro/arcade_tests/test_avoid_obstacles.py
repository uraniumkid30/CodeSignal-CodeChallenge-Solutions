from ..avoid_obstacles import solution
import unittest


class TestAvoidObstacles(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [5, 3, 6, 7, 9]
        expected_result: int = 4
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [5, 8, 9, 13, 14]
        expected_result: int = 6
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [19, 32, 11, 23]
        expected_result: int = 3
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [1000, 999]
        expected_result: int = 6
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [1, 4, 10, 6, 2]
        expected_result: int = 7
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
