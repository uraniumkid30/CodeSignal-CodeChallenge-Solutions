from ..shape_area import solution
import unittest


class TestShapeArea(unittest.TestCase):
    def test_case_1(self):
        inputnumber: int = 100
        expected_result: int = 19801
        result = solution(inputnumber)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputnumber: int = 8000
        expected_result: int = 127984001
        result = solution(inputnumber)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputnumber: int = 9998
        expected_result: int = 199900013
        result = solution(inputnumber)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputnumber: int = 8999
        expected_result: int = 161946005
        result = solution(inputnumber)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputnumber: int = 100
        expected_result: int = 19801
        result = solution(inputnumber)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
