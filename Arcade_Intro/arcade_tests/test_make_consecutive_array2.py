from ..make_array_consecutive_2 import solution
import unittest


class TestMakeArrayConsecutive2(unittest.TestCase):
    def test_case_1(self):
        statues: list = [6, 2, 3, 8]
        expected_result: int = 3
        result = solution(statues)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        statues: list = [0, 3]
        expected_result: int = 2
        result = solution(statues)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        statues: list = [5, 4, 6]
        expected_result: int = 0
        result = solution(statues)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        statues: list = [6, 3]
        expected_result: int = 2
        result = solution(statues)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        statues: list = [1]
        expected_result: int = 0
        result = solution(statues)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
