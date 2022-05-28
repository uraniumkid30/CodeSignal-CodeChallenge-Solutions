from ..are_similar import solution
import unittest


class TestAdjacentElementProduct(unittest.TestCase):
    def test_case_1(self):
        inputArray_a: list = [1, 1, 4]
        inputArray_b: list = [1, 2, 4]
        expected_result: bool = False
        result = solution(inputArray_a, inputArray_b)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray_a: list = [2, 3, 1]
        inputArray_b: list = [1, 3, 2]
        expected_result: bool = True
        result = solution(inputArray_a, inputArray_b)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray_a: list = [2, 3, 9]
        inputArray_b: list = [10, 3, 2]
        expected_result: bool = False
        result = solution(inputArray_a, inputArray_b)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray_a: list = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
        inputArray_b: list = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
        expected_result: bool = True
        result = solution(inputArray_a, inputArray_b)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray_a: list = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
        inputArray_b: list = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
        expected_result: bool = False
        result = solution(inputArray_a, inputArray_b)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
