#!/usr/bin/env python

import unittest

from classes import Hand
from modules import poker_game


class TestGame(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_run_game_five_card_draw_pass(self):
        score_card = poker_game.run_game_five_card_draw('2c 3d 4h 5s 6c')
        self.assertEqual(score_card.score, '40605040302')
        self.assertEqual(score_card.hand_rank, 4)
        self.assertEqual(score_card.hand.print_alpha(), '6C 5S 4H 3D 2C')

    def test_run_game_texas_hold_em_pass(self):
        score_card = poker_game.run_game_texas_hold_em('2c 3d 4h 5s 6c 7d 8h')
        self.assertEqual(score_card.score, '40807060504')
        self.assertEqual(score_card.hand_rank, 4)
        self.assertEqual(score_card.hand.print_alpha(), '8H 7D 6C 5S 4H')


if __name__ == '__main__':
    unittest.main()
