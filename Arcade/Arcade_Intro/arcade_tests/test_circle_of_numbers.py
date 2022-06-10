from ..circle_of_numbers import solution
import unittest


class TestCircleOfNumbers(unittest.TestCase):
    def test_case_1(self):
        n: int = 10
        first_number: int = 2
        expected_result: int = 7
        result = solution(n, first_number)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        n: int = 4
        first_number: int = 1
        expected_result: int = 3
        result = solution(n, first_number)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        n: int = 18
        first_number: int = 6
        expected_result: int = 15
        result = solution(n, first_number)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        n: int = 12
        first_number: int = 10
        expected_result: int = 4
        result = solution(n, first_number)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        n: int = 10
        first_number: int = 7
        expected_result: int = 2
        result = solution(n, first_number)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
