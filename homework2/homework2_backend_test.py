from homework2_backend import Game
import unittest

class GameTest(unittest.TestCase):
    def test_check_win_con(self):
        game = Game()
        self.assertEqual(game.check_board_state(('x','x','x',4,5,6,7,8,9)), 'x')

if __name__ == '__main__':
    unittest.main()