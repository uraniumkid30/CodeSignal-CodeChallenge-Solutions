from ..variable_name import solution, solution_v2
import unittest


class TestVariableName(unittest.TestCase):
    def test_case_1(self):
        inputString: str = "var_1__Int"
        expected_result: bool = True
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputString: str = "qq-q"
        expected_result: bool = False
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputString: str = "2w2"
        expected_result: bool = False
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputString: str = "va[riable0"
        expected_result: bool = False
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputString: str = "_Aas_23"
        expected_result: bool = True
        result = solution(inputString)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
