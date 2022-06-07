from ..array_replace import solution
import unittest


class TestArrayReplace(unittest.TestCase):
    def test_case_1(self):
        inputArray: list = [1, 2, 1]
        elemToReplace: int = 1
        substitutionElem: int = 3
        expected_result: list = [3, 2, 3]
        result = solution(inputArray, elemToReplace, substitutionElem)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputArray: list = [1, 2, 3, 4, 5]
        elemToReplace: int = 3
        substitutionElem: int = 0
        expected_result: list = [1, 2, 0, 4, 5]
        result = solution(inputArray, elemToReplace, substitutionElem)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputArray: list = [1, 1, 1]
        elemToReplace: int = 1
        substitutionElem: int = 10
        expected_result: list = [10, 10, 10]
        result = solution(inputArray, elemToReplace, substitutionElem)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputArray: list = [1, 2, 1, 2, 1]
        elemToReplace: int = 2
        substitutionElem: int = 1
        expected_result: list = [1, 1, 1, 1, 1]
        result = solution(inputArray, elemToReplace, substitutionElem)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputArray: list = [1, 2, 1, 2, 1]
        elemToReplace: int = 2
        substitutionElem: int = 2
        expected_result: list = [1, 2, 1, 2, 1]
        result = solution(inputArray, elemToReplace, substitutionElem)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
