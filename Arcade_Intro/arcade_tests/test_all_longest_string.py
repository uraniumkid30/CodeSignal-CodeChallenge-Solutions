from ..all_longest_string import solution
import unittest


class TestAdjacentElementProduct(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = ["aba", "aa", "ad", "vcd", "aba"]
        expected_result: list = ["aba", "vcd", "aba"]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [
            "young",
            "yooooooung",
            "hot",
            "or",
            "not",
            "come",
            "on",
            "fire",
            "water",
            "watermelon",
        ]
        expected_result: list = ["yooooooung", "watermelon"]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = ["enyky", "benyky", "yely", "varennyky"]
        expected_result: list = ["varennyky"]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [
            "a",
            "abc",
            "cbd",
            "zzzzzz",
            "a",
            "abcdef",
            "asasa",
            "aaaaaa",
        ]
        expected_result: list = ["zzzzzz", "abcdef", "aaaaaa"]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = ["abc", "eeee", "abcd", "dcd"]
        expected_result: list = ["eeee", "abcd"]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
