from ..strings_rearrangement import solution
import unittest


class TestStringRearrangement(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = ["abc", "abx", "axx", "abx", "abc"]
        expected_result: bool = True
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = ["abc", "abx", "axx", "abc"]
        expected_result: bool = False
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = ["ab", "ad", "ef", "eg"]
        expected_result: bool = False
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = ["f", "g", "a", "h"]
        expected_result: bool = True
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = ["ff", "gf", "af", "ar", "hf"]
        expected_result: bool = True
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
