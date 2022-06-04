from ..are_equally_strong import solution
import unittest


class TestAreEquallyStrong(unittest.TestCase):
    def test_case_1(self):
        yourLeft: int = 10
        yourRight: int = 15
        friendsLeft: int = 15
        friendsRight: int = 10
        expected_result: bool = True
        result = solution(yourLeft, yourRight, friendsLeft, friendsRight)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        yourLeft: int = 15
        yourRight: int = 10
        friendsLeft: int = 15
        friendsRight: int = 9
        expected_result: bool = False
        result = solution(yourLeft, yourRight, friendsLeft, friendsRight)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        yourLeft: int = 15
        yourRight: int = 10
        friendsLeft: int = 15
        friendsRight: int = 10
        expected_result: bool = True
        result = solution(yourLeft, yourRight, friendsLeft, friendsRight)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        yourLeft: int = 10
        yourRight: int = 5
        friendsLeft: int = 5
        friendsRight: int = 10
        expected_result: bool = True
        result = solution(yourLeft, yourRight, friendsLeft, friendsRight)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        yourLeft: int = 20
        yourRight: int = 15
        friendsLeft: int = 5
        friendsRight: int = 20
        expected_result: bool = True
        result = solution(yourLeft, yourRight, friendsLeft, friendsRight)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
