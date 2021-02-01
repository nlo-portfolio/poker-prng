#!/usr/bin/env python

import unittest

from classes import Rank


class TestRank(unittest.TestCase):

    def setUp(self):
        self.two = Rank.Rank(2)
        self.five = Rank.Rank(5)
        self.ten = Rank.Rank(10)
        self.jack = Rank.Rank(11)
        self.queen = Rank.Rank(12)
        self.king = Rank.Rank(13)
        self.ace = Rank.Rank(14)

    def tearDown(self):
        pass

    def test_init_lowercase(self):
        jack = Rank.Rank(11)
        self.assertEqual(jack, 11)
        queen = Rank.Rank(12)
        self.assertEqual(queen, 12)
        king = Rank.Rank(13)
        self.assertEqual(king, 13)
        ace = Rank.Rank(14)
        self.assertEqual(ace, 14)

    def test_lt_comp_pass(self):
        self.assertTrue(self.two < self.five)
        self.assertTrue(self.five < self.ten)
        self.assertTrue(self.ten < self.jack)
        self.assertTrue(self.jack < self.queen)
        self.assertTrue(self.queen < self.king)
        self.assertTrue(self.king < self.ace)

    def test_lt_comp_fail(self):
        self.assertFalse(self.five < self.two)
        self.assertFalse(self.ten < self.five)
        self.assertFalse(self.jack < self.ten)
        self.assertFalse(self.queen < self.jack)
        self.assertFalse(self.king < self.queen)
        self.assertFalse(self.ace < self.king)

    def test_lt_comp_eq_fail(self):
        self.assertFalse(self.two < self.two)
        self.assertFalse(self.five < self.five)
        self.assertFalse(self.ten < self.ten)
        self.assertFalse(self.jack < self.jack)
        self.assertFalse(self.queen < self.queen)
        self.assertFalse(self.king < self.king)
        self.assertFalse(self.ace < self.ace)

    def test_gt_comp_pass(self):
        self.assertTrue(self.ace > self.king)
        self.assertTrue(self.king > self.queen)
        self.assertTrue(self.queen > self.jack)
        self.assertTrue(self.jack > self.ten)
        self.assertTrue(self.ten > self.five)
        self.assertTrue(self.five > self.two)

    def test_gt_comp_fail(self):
        self.assertFalse(self.two > self.five)
        self.assertFalse(self.five > self.ten)
        self.assertFalse(self.ten > self.jack)
        self.assertFalse(self.jack > self.queen)
        self.assertFalse(self.queen > self.king)
        self.assertFalse(self.king > self.ace)

    def test_gt_comp_eq_fail(self):
        self.assertFalse(self.two > self.two)
        self.assertFalse(self.five > self.five)
        self.assertFalse(self.ten > self.ten)
        self.assertFalse(self.jack > self.jack)
        self.assertFalse(self.queen > self.queen)
        self.assertFalse(self.king > self.king)
        self.assertFalse(self.ace > self.ace)

    def test_eq_comp_pass(self):
        self.assertTrue(self.two == self.two)
        self.assertTrue(self.five == self.five)
        self.assertTrue(self.ten == self.ten)
        self.assertTrue(self.jack == self.jack)
        self.assertTrue(self.queen == self.queen)
        self.assertTrue(self.king == self.king)
        self.assertTrue(self.ace == self.ace)

    def test_eq_comp_ne_pass(self):
        self.assertTrue(self.two != self.five)
        self.assertTrue(self.five != self.ten)
        self.assertTrue(self.ten != self.jack)
        self.assertTrue(self.jack != self.queen)
        self.assertTrue(self.queen != self.king)
        self.assertTrue(self.king != self.ace)

    def test_eq_comp_ne_fail(self):
        self.assertFalse(self.two == self.five)
        self.assertFalse(self.five == self.ten)
        self.assertFalse(self.ten == self.jack)
        self.assertFalse(self.jack == self.queen)
        self.assertFalse(self.queen == self.king)
        self.assertFalse(self.king == self.ace)

    def test_eq_comp_eq_fail(self):
        self.assertFalse(self.two != self.two)
        self.assertFalse(self.five != self.five)
        self.assertFalse(self.ten != self.ten)
        self.assertFalse(self.jack != self.jack)
        self.assertFalse(self.queen != self.queen)
        self.assertFalse(self.king != self.king)
        self.assertFalse(self.ace != self.ace)


if __name__ == '__main__':
    unittest.main()
