import unittest
import tic_tac_toe


class TestTicTacToe(unittest.TestCase):

    def test_if_empty_board_is_not_full(self):
        board = [[' . ', ' . ', ' . '], [' . ', ' . ', ' . '], [' . ', ' . ', ' . ']]
        self.assertFalse(tic_tac_toe.is_full(board))

    def test_if_full_board_is_full(self):
        board = [[' X ', ' X ', ' X '], [' X ', ' X ', ' X '], [' X ', ' X ', ' X ']]
        self.assertTrue(tic_tac_toe.is_full(board))

    def test_if_half_full_board_is_not_full(self):
        board = [[' . ', ' X ', ' . '], [' X ', ' . ', ' X '], [' . ', ' X ', ' . ']]
        self.assertFalse(tic_tac_toe.is_full(board))

    def test_search_ai_move(self):
        board = [[' X ', ' X ', ' X '], [' X ', ' X ', ' X '], [' X ', ' X ', ' . ']]
        self.assertFalse(tic_tac_toe.is_full(board))
        self.assertEqual(tic_tac_toe.get_ai_move(board, 0), (2, 2))

    def test_search_ai_move_with_more_empty_cell(self):
        board = [[' X ', ' . ', ' . '], [' X ', ' X ', ' . '], [' X ', ' X ', ' . ']]
        moves = [(0, 1), (0, 2), (1, 2), (2, 2)]
        self.assertTrue(tic_tac_toe.get_ai_move(board, 0) in moves)

    def test_search_ai_move_if_board_is_full(self):
        board = [[' X ', ' X ', ' X '], [' X ', ' X ', ' X '], [' X ', ' X ', ' X ']]
        self.assertIsNone(tic_tac_toe.get_ai_move(board, 0))

    def test_if_board_is_full_player_move_return_true(self):
        board = [[' X ', ' X ', ' X '], [' X ', ' X ', ' X '], [' X ', ' X ', ' . ']]
        self.assertTrue(tic_tac_toe.player_move(board, 0, dummy_move_function))

    def test_if_board_is_not_full_player_move_return_none(self):
        board = [[' X ', ' X ', ' X '], [' X ', ' X ', ' X '], [' . ', ' X ', ' . ']]
        self.assertIsNone(tic_tac_toe.player_move(board, 0, dummy_move_function))

    def test_get_smart_ai_move_correct_row_move(self):
        board = [[' X ', ' X ', ' . '], [' . ', ' . ', ' X '], [' . ', ' X ', ' . ']]
        self.assertEqual(tic_tac_toe.get_smart_ai_move(board, " X "), (0, 2))

    def test_get_smart_ai_move_correct_column_move(self):
        board = [[' X ', ' . ', ' . '], [' X ', ' . ', ' . '], [' . ', ' . ', ' . ']]
        self.assertEqual(tic_tac_toe.get_smart_ai_move(board, " X "), (2, 0))

    def test_get_smart_ai_move_correct_diagonal_move(self):
        board = [[' X ', ' . ', ' . '], [' . ', ' X ', ' . '], [' . ', ' . ', ' . ']]
        self.assertEqual(tic_tac_toe.get_smart_ai_move(board, " X "), (2, 2))


def dummy_move_function(board, player):
    return 2, 2


if __name__ == '__main__':
    unittest.main()
