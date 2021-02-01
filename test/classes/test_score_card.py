#!/usr/bin/env python

from classes import ScoreCard

import unittest

from classes import Hand
from classes import ScoreCard


class TestScoreCard(unittest.TestCase):

    def setUp(self):
        hand = Hand.Hand.parse_str('AS QH KD JC 10H')
        self.score_card = ScoreCard.ScoreCard(hand, 4)

    def tearDown(self):
        pass

    def test_calc_score_pass(self):
        self.assertEqual(self.score_card.calc_score(), str(41412131110))

    def test_hand_str_pass(self):
        self.assertEqual(self.score_card.hand_str(), 'Straight')

    def test_lt_pass(self):
        hand_two = Hand.Hand.parse_str('9S 10S JS QS KS')
        score_card_two = ScoreCard.ScoreCard(hand_two, 8)
        self.assertTrue(self.score_card < score_card_two)

    def test_gt_pass(self):
        hand_two = Hand.Hand.parse_str('2S 5H 5C AH AH')
        score_card_two = ScoreCard.ScoreCard(hand_two, 2)
        self.assertTrue(self.score_card > score_card_two)

    def test_eq_pass(self):
        hand_two = Hand.Hand.parse_str('AS QH KD JC 10H')
        score_card_two = ScoreCard.ScoreCard(hand_two, 4)
        self.assertTrue(self.score_card == score_card_two)


if __name__ == '__main__':
    unittest.main()
