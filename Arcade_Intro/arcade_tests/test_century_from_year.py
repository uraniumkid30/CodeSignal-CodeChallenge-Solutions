from ..century_from_year import solution
import unittest


class TestExtractEachKth(unittest.TestCase):
    def test_case_1(self):
        year: int = 1905
        expected_result: int = 20
        result = solution(year)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        year: int = 1700
        expected_result: int = 17
        result = solution(year)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        year: int = 1988
        expected_result: int = 20
        result = solution(year)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        year: int = 2000
        expected_result: int = 20
        result = solution(year)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        year: int = 2001
        expected_result: int = 21
        result = solution(year)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
