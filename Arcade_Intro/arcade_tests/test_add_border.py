from ..add_border import solution
import unittest


class TestAdjacentElementProduct(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = ["abc", "ded"]
        expected_result: list = ["*****", "*abc*", "*ded*", "*****"]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = ["a"]
        expected_result: list = ["***", "*a*", "***"]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = ["aa", "**", "zz"]
        expected_result: list = ["****", "*aa*", "****", "*zz*", "****"]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = ["abcde", "fghij", "klmno", "pqrst", "uvwxy"]
        expected_result: list = [
            "*******",
            "*abcde*",
            "*fghij*",
            "*klmno*",
            "*pqrst*",
            "*uvwxy*",
            "*******",
        ]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = ["wzy**"]
        expected_result: list = ["*******", "*wzy***", "*******"]
        result = solution(inputArray)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
