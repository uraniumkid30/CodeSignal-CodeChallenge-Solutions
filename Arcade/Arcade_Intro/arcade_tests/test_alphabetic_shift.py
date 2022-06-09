from ..alphabetice_shift import solution
import unittest


class TestAlphabeticShift(unittest.TestCase):
    def test_case_1(self):
        text: str = "crazy"
        expected_result: str = "dsbaz"
        result = solution(text)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        text: str = "z"
        expected_result: str = "a"
        result = solution(text)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        text: str = "aaaabbbccd"
        expected_result: str = "bbbbcccdde"
        result = solution(text)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        text: str = "fuzzy"
        expected_result: str = "gvaaz"
        result = solution(text)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        text: str = "codesignal"
        expected_result: str = "dpeftjhobm"
        result = solution(text)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
