#!/usr/bin/env python

'''
This class is responsible for testing the 10 basic hands:
0. High Card
1. Pair
2. 2 Pair
3. Three of a Kind
4. Straight
5. Flush
6. Full House
7. Four of a Kind
8. Straight Flush
9. Royal Straight Flush (Ace high straight flush)

Hand cards are selected to test the upper and lower bounds of the histogram
list, and are inserted in the opposite of the desired order to test proper
arrangement for the scoring function.
'''

import sys
import unittest

from classes import Hand
from classes import HandEval


class TestHandEval(unittest.TestCase):

    def setUp(self):
        self.hand_eval = HandEval.HandEval()

    def tearDown(self):
        pass

    def test_royal_straight_flush_pass(self):
        score_card = self.hand_eval.evaluate_hand(Hand.Hand.parse_str('10S JS QS KS AS'))
        self.assertEqual(score_card.hand_rank, 9)

    def test_straight_flush_pass(self):
        score_card = self.hand_eval.evaluate_hand(Hand.Hand.parse_str('7D 8D 9D 10D JD'))
        self.assertEqual(score_card.hand_rank, 8)

    def test_four_of_a_kind_pass(self):
        score_card = self.hand_eval.evaluate_hand(Hand.Hand.parse_str('AC AH AD AC 2S'))
        self.assertEqual(score_card.hand_rank, 7)

    def test_full_house_pass(self):
        score_card = self.hand_eval.evaluate_hand(Hand.Hand.parse_str('2D 2C AS AC AD'))
        self.assertEqual(score_card.hand_rank, 6)

    def test_flush_pass(self):
        score_card = self.hand_eval.evaluate_hand(Hand.Hand.parse_str('3S 10S 5S 8S AS'))
        self.assertEqual(score_card.hand_rank, 5)

    def test_straight_pass(self):
        score_card = self.hand_eval.evaluate_hand(Hand.Hand.parse_str('AS QH KD JC 10H'))
        self.assertEqual(score_card.hand_rank, 4)

    def test_straight_ace_low_pass(self):
        score_card = self.hand_eval.evaluate_hand(Hand.Hand.parse_str('AS 2H 3D 4C 5H'))
        self.assertEqual(score_card.hand_rank, 4)

    def test_three_of_a_kind_pass(self):
        score_card = self.hand_eval.evaluate_hand(Hand.Hand.parse_str('4C QD AC AH AS'))
        self.assertEqual(score_card.hand_rank, 3)

    def test_two_pair_pass(self):
        score_card = self.hand_eval.evaluate_hand(Hand.Hand.parse_str('2S 5H 5C AH AH'))
        self.assertEqual(score_card.hand_rank, 2)

    def test_pair_pass(self):
        score_card = self.hand_eval.evaluate_hand(Hand.Hand.parse_str('JS 10D 4H AD AC'))
        self.assertEqual(score_card.hand_rank, 1)

    def test_high_card_pass(self):
        score_card = self.hand_eval.evaluate_hand(Hand.Hand.parse_str('2S 10D 4H 8D AC'))
        self.assertEqual(score_card.hand_rank, 0)


if __name__ == '__main__':
    unittest.main()
