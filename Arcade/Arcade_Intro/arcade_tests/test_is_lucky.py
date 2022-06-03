from ..is_lucky import solution
import unittest


class TestExtractEachKth(unittest.TestCase):
    def test_case_1(self):
        n: int = 123321
        expected_result: bool = True
        result = solution(n)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        n: int = 1010
        expected_result: bool = True
        result = solution(n)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        n: int = 261534
        expected_result: bool = False
        result = solution(n)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        n: int = 100000
        expected_result: bool = False
        result = solution(n)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        n: int = 999999
        expected_result: bool = True
        result = solution(n)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
