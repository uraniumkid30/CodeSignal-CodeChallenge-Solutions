from ..is_ipv4_address import solution
import unittest


class TestIsIPv4Address(unittest.TestCase):
    def test_case_1(self):
        inputString: str = "172.16.254.1"
        expected_result: bool = True
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        inputString: str = "172.316.254.1"
        expected_result: bool = False
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        inputString: str = "0..1.0.0"
        expected_result: bool = False
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        inputString: str = "7283728"
        expected_result: bool = False
        result = solution(inputString)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        inputString: str = "255.255.255.255abcdekjhf"
        expected_result: bool = False
        result = solution(inputString)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
