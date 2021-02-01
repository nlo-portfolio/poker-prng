#!/usr/bin/env python

import unittest

from classes import Suit


class TestSuit(unittest.TestCase):

    def setUp(self):
        self.club = Suit.Suit('C')
        self.diamond = Suit.Suit('D')
        self.heart = Suit.Suit('H')
        self.spade = Suit.Suit('S')

    def tearDown(self):
        pass

    def test_init_lowercase(self):
        club = Suit.Suit('c')
        self.assertEqual(self.club, club)
        diamond = Suit.Suit('d')
        self.assertEqual(self.diamond, diamond)
        heart = Suit.Suit('h')
        self.assertEqual(self.heart, heart)
        spade = Suit.Suit('s')
        self.assertEqual(self.spade, spade)

    def test_lt_comp_pass(self):
        self.assertTrue(self.club < self.diamond)
        self.assertTrue(self.diamond < self.heart)
        self.assertTrue(self.heart < self.spade)

    def test_lt_comp_fail(self):
        self.assertFalse(self.spade < self.heart)
        self.assertFalse(self.heart < self.diamond)
        self.assertFalse(self.diamond < self.club)

    def test_lt_comp_eq_fail(self):
        self.assertFalse(self.club < self.club)
        self.assertFalse(self.diamond < self.diamond)
        self.assertFalse(self.heart < self.heart)
        self.assertFalse(self.spade < self.spade)

    def test_gt_comp_pass(self):
        self.assertTrue(self.spade > self.heart)
        self.assertTrue(self.heart > self.diamond)
        self.assertTrue(self.diamond > self.club)

    def test_gt_comp_fail(self):
        self.assertFalse(self.club > self.diamond)
        self.assertFalse(self.diamond > self.heart)
        self.assertFalse(self.heart > self.spade)

    def test_gt_comp_eq_fail(self):
        self.assertFalse(self.club > self.club)
        self.assertFalse(self.diamond > self.diamond)
        self.assertFalse(self.heart > self.heart)
        self.assertFalse(self.spade > self.spade)

    def test_eq_comp_pass(self):
        self.assertTrue(self.club == self.club)
        self.assertTrue(self.diamond == self.diamond)
        self.assertTrue(self.heart == self.heart)
        self.assertTrue(self.spade == self.spade)

    def test_eq_comp_ne_pass(self):
        self.assertTrue(self.club != self.diamond)
        self.assertTrue(self.diamond != self.heart)
        self.assertTrue(self.heart != self.spade)

    def test_eq_comp_ne_fail(self):
        self.assertFalse(self.club == self.diamond)
        self.assertFalse(self.diamond == self.heart)
        self.assertFalse(self.heart == self.spade)

    def test_eq_comp_eq_fail(self):
        self.assertFalse(self.club != self.club)
        self.assertFalse(self.diamond != self.diamond)
        self.assertFalse(self.heart != self.heart)
        self.assertFalse(self.spade != self.spade)


if __name__ == '__main__':
    unittest.main()
