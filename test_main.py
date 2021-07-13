#For some reason main.py runs when this runs so comment out the main section in main.py

import unittest
from main import new_board
from main import is_valid_move
from main import check_winner

class TestMain(unittest.TestCase):

    def test_is_valid_move(self):
        board = new_board()
        board[0][0] = 'X'; board[1][1] = 'O'

        self.assertFalse(is_valid_move(board, (-1,0)))
        self.assertFalse(is_valid_move(board, (3,0)))
        self.assertFalse(is_valid_move(board, (0,-1)))
        self.assertFalse(is_valid_move(board, (0,3)))
        self.assertFalse(is_valid_move(board, (0,0)))
        self.assertFalse(is_valid_move(board, (1,1)))
        self.assertTrue(is_valid_move(board, (0,1)))
    
    def test_check_winner(self):
        board = new_board()
        board[0][0] = 'X'; board[1][0] = 'O'; board[2][0] = 'X'
        board[0][1] = 'O'; board[1][1] = 'O'; board[2][1] = 'X'
        board[0][2] = 'X'; board[1][2] = 'X'; board[2][2] = 'O'

        self.assertFalse(check_winner(board))

        board = new_board()
        board[0][0] = None; board[1][0] = None; board[2][0] = None
        board[0][1] = None; board[1][1] = None; board[2][1] = None
        board[0][2] = None; board[1][2] = None; board[2][2] = None

        self.assertFalse(check_winner(board))

        board = new_board()
        board[0][0] = 'X'; board[1][0] = None; board[2][0] = 'O'
        board[0][1] = None; board[1][1] = 'X'; board[2][1] = 'O'
        board[0][2] = None; board[1][2] = None; board[2][2] = 'X'

        self.assertTrue(check_winner(board))

        board = new_board()
        board[0][0] = 'X'; board[1][0] = None; board[2][0] = None
        board[0][1] = 'X'; board[1][1] = 'O'; board[2][1] = None
        board[0][2] = 'X'; board[1][2] = None; board[2][2] = 'O'

        self.assertTrue(check_winner(board))

        board = new_board()
        board[0][0] = None; board[1][0] = 'X'; board[2][0] = 'O'
        board[0][1] = None; board[1][1] = 'X'; board[2][1] = None
        board[0][2] = 'O'; board[1][2] = 'X'; board[2][2] = None

        self.assertTrue(check_winner(board))

        board = new_board()
        board[0][0] = 'O'; board[1][0] = None; board[2][0] = 'X'
        board[0][1] = None; board[1][1] = 'O'; board[2][1] = 'X'
        board[0][2] = None; board[1][2] = None; board[2][2] = 'X'

        self.assertTrue(check_winner(board))

        board = new_board()
        board[0][0] = 'X'; board[1][0] = 'X'; board[2][0] = 'X'
        board[0][1] = None; board[1][1] = 'O'; board[2][1] = None
        board[0][2] = None; board[1][2] = None; board[2][2] = 'O'

        self.assertTrue(check_winner(board))

        board = new_board()
        board[0][0] = 'X'; board[1][0] = None; board[2][0] = None
        board[0][1] = 'O'; board[1][1] = 'O'; board[2][1] = 'O'
        board[0][2] = None; board[1][2] = None; board[2][2] = 'X'

        self.assertTrue(check_winner(board))

        board = new_board()
        board[0][0] = 'X'; board[1][0] = None; board[2][0] = None
        board[0][1] = None; board[1][1] = 'X'; board[2][1] = None
        board[0][2] = 'O'; board[1][2] = 'O'; board[2][2] = 'O'

        self.assertTrue(check_winner(board))

        board = new_board()
        board[0][0] = 'X'; board[1][0] = None; board[2][0] = 'O'
        board[0][1] = None; board[1][1] = 'O'; board[2][1] = None
        board[0][2] = 'O'; board[1][2] = None; board[2][2] = 'X'

        self.assertTrue(check_winner(board))

#to run it as simply "python test_main.py"
if __name__ == '__main__':
    unittest.main()