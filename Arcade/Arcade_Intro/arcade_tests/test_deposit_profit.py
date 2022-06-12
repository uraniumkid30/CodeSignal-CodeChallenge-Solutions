from ..deposit_profit import solution
import unittest


class TestDepositProfit(unittest.TestCase):
    def test_case_1(self):
        deposit: int = 100
        rate: int = 20
        threshold: int = 70
        expected_result: int = 3
        result = solution(deposit, rate, threshold)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        deposit: int = 100
        rate: int = 1
        threshold: int = 101
        expected_result: int = 1
        result = solution(deposit, rate, threshold)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        deposit: int = 6
        rate: int = 100
        threshold: int = 64
        expected_result: int = 3
        result = solution(deposit, rate, threshold)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        deposit: int = 20
        rate: int = 20
        threshold: int = 50
        expected_result: int = 6
        result = solution(deposit, rate, threshold)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        deposit: int = 50
        rate: int = 25
        threshold: int = 100
        expected_result: int = 4
        result = solution(deposit, rate, threshold)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
