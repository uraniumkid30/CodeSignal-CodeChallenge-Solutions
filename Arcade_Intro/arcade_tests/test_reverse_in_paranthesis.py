from ..reverse_in_paranthesis import solution
import unittest


class TestMakeArrayConsecutive2(unittest.TestCase):
    def test_case_1(self):
        text: str = "foo(bar)baz"
        expected_result: str = "foorabbaz"
        result = solution(text)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        text: str = "()"
        expected_result: str = ""
        result = solution(text)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        text: str = ""
        expected_result: str = ""
        result = solution(text)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        text: str = "foo(bar(baz))blim"
        expected_result: str = "foobazrabblim"
        result = solution(text)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        text: str = "foo(bar)baz(blim)"
        expected_result: str = "foorabbazmilb"
        result = solution(text)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
