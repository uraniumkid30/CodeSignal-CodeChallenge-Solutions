from ..chessboard_cell_color import solution
import unittest


class TestChessBoardCellColor(unittest.TestCase):
    def test_case_1(self):
        cell_a: str = "A1"
        cell_b: str = "C3"
        expected_result: bool = True
        result = solution(cell_a, cell_b)
        self.assertEqual(expected_result, result)

    def test_case_2(self):
        cell_a: str = "A1"
        cell_b: str = "H3"
        expected_result: bool = False
        result = solution(cell_a, cell_b)
        self.assertEqual(expected_result, result)

    def test_case_3(self):
        cell_a: str = "A1"
        cell_b: str = "A2"
        expected_result: bool = False
        result = solution(cell_a, cell_b)
        self.assertEqual(expected_result, result)

    def test_case_4(self):
        cell_a: str = "G5"
        cell_b: str = "E7"
        expected_result: bool = True
        result = solution(cell_a, cell_b)
        self.assertEqual(expected_result, result)

    def test_case_5(self):
        cell_a: str = "C3"
        cell_b: str = "B5"
        expected_result: bool = False
        result = solution(cell_a, cell_b)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
