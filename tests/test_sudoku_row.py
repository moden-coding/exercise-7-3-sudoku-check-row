#!/usr/bin/env python3

import unittest

from src.sudoku_row import row_correct


SUDOKU = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2],
]

# A second grid where several rows have been mutated to contain a
# repeated nonzero digit, used to exercise both the True and False paths.
CHECK_SUDOKU = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 2, 0, 0, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 4, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 6, 6],
    [3, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 2, 0, 2, 0, 1],
]


class TestRowCorrect(unittest.TestCase):

    def test_worked_example(self):
        result = row_correct(SUDOKU, 0)
        self.assertEqual(
            result, True,
            msg="row_correct(sudoku, 0) should be True for row 0 = %s: no "
                "nonzero digit is repeated (zeros are blanks and don't "
                "count)." % (SUDOKU[0],))

    def test_return_type_is_bool(self):
        result = row_correct(SUDOKU, 0)
        self.assertIsInstance(
            result, bool,
            msg="row_correct(sudoku, 0) should return a bool, not %s. Got "
                "%r." % (type(result).__name__, result))

    def test_valid_rows(self):
        for row in [0, 3, 4, 5]:
            with self.subTest(row=row):
                result = row_correct(CHECK_SUDOKU, row)
                self.assertEqual(
                    result, True,
                    msg="row_correct(sudoku, %d) should be True for row "
                        "%s: no nonzero digit is repeated."
                        % (row, CHECK_SUDOKU[row]))

    def test_invalid_rows(self):
        for row in [1, 2, 6, 7, 8]:
            with self.subTest(row=row):
                result = row_correct(CHECK_SUDOKU, row)
                self.assertEqual(
                    result, False,
                    msg="row_correct(sudoku, %d) should be False for row "
                        "%s: a nonzero digit is repeated."
                        % (row, CHECK_SUDOKU[row]))

    def test_row_of_all_zeros_is_valid(self):
        blank_sudoku = [[0] * 9 for _ in range(9)]
        result = row_correct(blank_sudoku, 4)
        self.assertEqual(
            result, True,
            msg="row_correct(sudoku, 4) should be True when row 4 is all "
                "zeros: an empty row has no repeated nonzero digit.")


if __name__ == "__main__":
    unittest.main()
