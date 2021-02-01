#!/usr/bin/env python

import unittest

from classes import Card


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card_one = Card.Card(2, 'C')
        self.card_two = Card.Card(14, 'S')
        self.card_three = Card.Card(2, 'C')
        self.card_four = Card.Card(4, 'H')

    def tearDown(self):
        pass

    def test_lt_comp_pass(self):
        self.assertTrue(self.card_one < self.card_two)

    def test_lt_comp_fail(self):
        self.assertFalse(self.card_two < self.card_one)

    def test_lt_comp_equal_fail(self):
        self.assertFalse(self.card_one < self.card_three)

    def test_gt_comp_pass(self):
        self.assertTrue(self.card_two > self.card_one)

    def test_gt_comp_fail(self):
        self.assertFalse(self.card_one > self.card_two)

    def test_gt_comp_equal_fail(self):
        self.assertFalse(self.card_one > self.card_three)

    def test_eq_comp_pass(self):
        self.assertTrue(self.card_one == self.card_three)

    def test_eq_comp_eq_fail(self):
        self.assertFalse(self.card_one != self.card_three)

    def test_eq_comp_ne_pass(self):
        self.assertTrue(self.card_one != self.card_four)


if __name__ == '__main__':
    unittest.main()
