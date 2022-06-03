from ..common_character_count import solution
import unittest


class TestMakeArrayConsecutive2(unittest.TestCase):
    def test_case_1(self):
        phrase_a: str = "a"
        phrase_b: str = "aaa"
        expected_result: int = 1
        result = solution(phrase_a, phrase_b)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        phrase_a: str = "a"
        phrase_b: str = "b"
        expected_result: int = 0
        result = solution(phrase_a, phrase_b)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        phrase_a: str = "abca"
        phrase_b: str = "xyzbac"
        expected_result: int = 3
        result = solution(phrase_a, phrase_b)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        phrase_a: str = "zzzz"
        phrase_b: str = "zzzzzzz"
        expected_result: int = 4
        result = solution(phrase_a, phrase_b)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        phrase_a: str = "aabcc"
        phrase_b: str = "adcaa"
        expected_result: int = 3
        result = solution(phrase_a, phrase_b)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
