from ..even_digits_only import solution
import unittest


class TestEvenDigitsOnly(unittest.TestCase):
    def test_case_1(self):
        inputString: int = 248622
        expected_result: bool = True
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputString: int = 642386
        expected_result: bool = False
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputString: int = 248842
        expected_result: bool = True
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputString: int = 8
        expected_result: bool = True
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputString: int = 2462487
        expected_result: bool = False
        result = solution(inputString)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
