#!/usr/bin/env python

import unittest

from classes import Hand
from modules import hand_forge


class TestHand(unittest.TestCase):

    def setUp(self):
        self.hand = Hand.Hand.parse_str('AS AH AC KD KS JD 8H 5S 2H 4S')

    def tearDown(self):
        pass

    def test_validate_pass(self):
        self.assertTrue(Hand.Hand.validate('AS AH AC KD KS JD 8H 5S 2H 4S', 10))

    def test_validate_fail(self):
        self.assertFalse(Hand.Hand.validate('AS AH AC KD KS JD 8H 5S 2H 4S', 12))

    def test_validate_duplicates_fail(self):
        self.assertFalse(Hand.Hand.validate('2c 2c 3c 4c 5c', 5))

    def test_get_rank_histogram_pass(self):
        rank_histogram = self.hand.get_rank_histogram()
        self.assertEqual(rank_histogram[0], 1)
        self.assertEqual(rank_histogram[2], 1)
        self.assertEqual(rank_histogram[3], 1)
        self.assertEqual(rank_histogram[6], 1)
        self.assertEqual(rank_histogram[9], 1)
        self.assertEqual(rank_histogram[11], 2)
        self.assertEqual(rank_histogram[12], 3)

    def test_get_suit_histogram_pass(self):
        suit_histogram = self.hand.get_suit_histogram()
        self.assertEqual(suit_histogram[0], 1)
        self.assertEqual(suit_histogram[1], 2)
        self.assertEqual(suit_histogram[2], 3)
        self.assertEqual(suit_histogram[3], 4)

    def test_get_list_pass(self):
        self.assertEqual(self.hand.get_list(), list(self.hand.hand))

    def test_sort_pass(self):
        hand_sorted = Hand.Hand.parse_str('2H 4S 5S 8H JD KD KS AC AH AS')
        self.assertEqual(self.hand.sort().hand, hand_sorted.hand)

    def test_str_pass(self):
        pass


if __name__ == '__main__':
    unittest.main()
