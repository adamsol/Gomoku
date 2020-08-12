#!/usr/bin/env python

import unittest

from board import *


def _create_board(rows):
    board = Board(len(rows))
    expected = None

    for i, row in enumerate(rows):
        for j, c in enumerate(row):
            if c == 'O':
                board.put(i, j, Color.BLACK)
            elif c == 'X':
                board.put(i, j, Color.WHITE)
            elif c == '_':
                expected = (i, j)

    return board, expected


class GradeTests(unittest.TestCase):

    def test_grade_2(self):
        board, _ = _create_board([
            '       ',
            '       ',
            '       ',
            '   O   ',
            '       ',
            '   X   ',
            '       ',
        ])
        grade1 = board.grade(2, 4, Color.BLACK)
        self.assertGreater(grade1, 0)
        self.assertEqual(board.grade(3, 4, Color.BLACK), grade1)
        self.assertEqual(board.grade(4, 4, Color.BLACK), grade1)
        self.assertEqual(board.grade(4, 2, Color.BLACK), grade1)
        self.assertEqual(board.grade(3, 2, Color.BLACK), grade1)
        self.assertEqual(board.grade(2, 2, Color.BLACK), grade1)

        grade2 = board.grade(1, 5, Color.BLACK)
        self.assertGreater(grade1, grade2)
        self.assertEqual(board.grade(3, 5, Color.BLACK), grade2)
        self.assertEqual(board.grade(5, 5, Color.BLACK), grade2)
        self.assertEqual(board.grade(3, 1, Color.BLACK), grade2)
        self.assertEqual(board.grade(1, 1, Color.BLACK), grade2)

        grade3 = board.grade(4, 3, Color.BLACK)
        self.assertGreater(grade2, grade3)

    def test_grade_3(self):
        board, _ = _create_board([
            ' O O  ',
            '      ',
            ' XX   ',
            '      ',
            '   OO ',
            '    O ',
        ])
        grade1 = board.grade(0, 2, Color.BLACK)
        self.assertEqual(board.grade(2, 3, Color.WHITE), grade1)
        self.assertEqual(board.grade(4, 2, Color.BLACK), grade1)

        grade2 = board.grade(0, 4, Color.BLACK)
        self.assertEqual(board.grade(2, 4, Color.WHITE), grade2)

        grade3 = board.grade(2, 0, Color.WHITE)
        self.assertGreater(grade1, grade3)
        self.assertGreater(grade2, grade3)

    def test_grade_4(self):
        board, _ = _create_board([
            '      ',
            'X   OX',
            'X    X',
            'X O   ',
            ' O   X',
            '      ',
        ])
        grade1 = board.grade(4, 0, Color.WHITE)
        self.assertEqual(board.grade(2, 3, Color.BLACK), grade1)
        self.assertEqual(board.grade(3, 5, Color.WHITE), grade1)

        grade2 = board.grade(0, 0, Color.WHITE)
        self.assertGreater(grade1, grade2)

        grade3 = board.grade(5, 0, Color.WHITE)
        self.assertGreater(grade1, grade3)
        self.assertEqual(board.grade(0, 5, Color.BLACK), grade3)
        self.assertEqual(board.grade(0, 5, Color.WHITE), grade3)

    def test_grade_5(self):
        board, _ = _create_board([
            'OO OO',
            '     ',
            'XXX X',
            '     ',
            'OOOOO',
        ])
        grade = board.grade(0, 2, Color.BLACK)
        self.assertEqual(board.grade(2, 3, Color.WHITE), grade)
        self.assertEqual(board.grade(4, 0, Color.BLACK), grade)
        self.assertGreater(grade, board.grade(2, 3, Color.BLACK))

    def test_grade_6(self):
        board, _ = _create_board([
            'O    X',
            'O    X',
            'O     ',
            'O    X',
            '     X',
            'O    X',
        ])
        self.assertEqual(board.grade(4, 0, Color.BLACK), 0)
        self.assertEqual(board.grade(5, 2, Color.WHITE), 0)


class AITests(unittest.TestCase):

    def _test_ai(self, rows):
        board, expected = _create_board(rows)
        self.assertEqual(board.ai(Color.BLACK), expected)

    def test_defence_3(self):
        self._test_ai([
            '      ',
            ' XOO  ',
            '  X   ',
            '   _  ',
            '      ',
            '      ',
        ])

    def test_defence_3x3(self):
        self._test_ai([
            '        ',
            '     XX ',
            '    O   ',
            '   X    ',
            '  X_X O ',
            '   X    ',
            '        ',
            '        ',
        ])

    def test_defence_4(self):
        self._test_ai([
            '      ',
            ' XXX_ ',
            '  O   ',
            '  OO  ',
            '  O   ',
            '      ',
        ])

    def test_defence_4x3(self):
        self._test_ai([
            'X       ',
            ' X X    ',
            '  XX    ',
            '   _    ',
            '     O  ',
            '     O  ',
            '  OO    ',
            '        ',
        ])

    def test_defence_4x4(self):
        self._test_ai([
            '      X',
            '       ',
            '   XX  ',
            '   _X  ',
            '  XO   ',
            '    O  ',
            'X      ',
        ])

    def test_defence_5(self):
        self._test_ai([
            'XO  O ',
            'X O   ',
            'X  OOO',
            '_ OO O',
            'X OOO ',
            '      ',
        ])

    def test_defence_6(self):
        self._test_ai([
            '      ',
            '    X ',
            '  O X ',
            '  O _ ',
            'XX XXX',
            '      ',
        ])

    def test_offence_3(self):
        self._test_ai([
            '      ',
            '      ',
            ' OO_  ',
            '  X   ',
            '      ',
            '      ',
        ])

    def test_offence_3x3(self):
        self._test_ai([
            'X       ',
            'X  X X  ',
            'X   XX  ',
            '   O    ',
            '  O_O   ',
            '   O    ',
            '        ',
            '        ',
        ])

    def test_offence_4(self):
        self._test_ai([
            '       ',
            'O  X   ',
            '_   X X',
            'O XXX  ',
            'O   XX ',
            '   X X ',
            '     X ',
        ])

    def test_offence_4x3(self):
        self._test_ai([
            'X     X ',
            ' X X X  ',
            '  XX    ',
            ' XX X   ',
            '  XX O  ',
            '     O  ',
            ' XOOO_ X',
            '        ',
        ])

    def test_offence_4x4(self):
        self._test_ai([
            '       ',
            '       ',
            'O O_O O',
            '    X  ',
            '   X   ',
            '   XXX ',
            ' X     ',
        ])

    def test_offence_5(self):
        self._test_ai([
            ' XXXX ',
            'X XXXO',
            'XX XO ',
            'XXXOX ',
            'XXO   ',
            ' _    ',
        ])

    def test_offence_6(self):
        self._test_ai([
            'O     ',
            ' O  _ ',
            '  OO  ',
            '  OO  ',
            ' O   O',
            '     O',
        ])


class WinnerTests(unittest.TestCase):

    def test_winner_4(self):
        board, _ = _create_board([
            'XXXX ',
            '     ',
            '     ',
            '     ',
            '     ',
        ])
        self.assertEqual(board.winner, Color.NONE)

    def test_winner_interrupted(self):
        board, _ = _create_board([
            'O    ',
            ' O   ',
            'XOXXX',
            '   O ',
            '    O',
        ])
        self.assertEqual(board.winner, Color.NONE)

    def test_winner_5(self):
        board, _ = _create_board([
            '     ',
            'OOOOO',
            '     ',
            '     ',
            '     ',
        ])
        self.assertEqual(board.winner, Color.BLACK)

    def test_winner_5_blocked(self):
        board, _ = _create_board([
            '       ',
            '     X ',
            '    X  ',
            '   X   ',
            '  X    ',
            ' X     ',
            'O      ',
        ])
        self.assertEqual(board.winner, Color.WHITE)

    def test_winner_5x5(self):
        board, _ = _create_board([
            ' O     ',
            '  O O  ',
            '  XOO  ',
            '  X O  ',
            '  X OO ',
            '  X O  ',
            '       ',
        ])
        self.assertEqual(board.winner, Color.BLACK)

    def test_winner_6(self):
        board, _ = _create_board([
            'O    X',
            'O    X',
            'O    X',
            'O    X',
            'O    X',
            'O    X',
        ])
        self.assertEqual(board.winner, Color.NONE)


class DrawTests(unittest.TestCase):

    def test_draw(self):
        board, _ = _create_board([
            'XO',
            'OX',
        ])
        self.assertEqual(board.winner, Color.NONE)
        self.assertIsNone(board.ai(Color.WHITE))


if __name__ == '__main__':
    unittest.main()
