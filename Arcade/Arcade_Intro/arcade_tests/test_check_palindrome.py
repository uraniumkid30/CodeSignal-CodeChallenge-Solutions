from ..check_palindrome import solution, solution_v2
import unittest


class TestCheckPalindrome(unittest.TestCase):
    def test_case_1(self):
        inputString: str = "aabaa"
        expected_result: bool = True
        result = solution(inputString)
        self.assertEqual(expected_result, result)
        result = solution_v2(inputString)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputString: str = "hlbeeykoqqqqokyeeblh"
        expected_result: bool = True
        result = solution(inputString)
        self.assertEqual(expected_result, result)
        result = solution_v2(inputString)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputString: str = "zzzazzazz"
        expected_result: bool = False
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputString: str = "z"
        expected_result: bool = True
        result = solution(inputString)
        self.assertEqual(expected_result, result)
        result = solution_v2(inputString)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputString: str = "az"
        expected_result: bool = False
        result = solution(inputString)
        self.assertEqual(expected_result, result)
        result = solution_v2(inputString)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
