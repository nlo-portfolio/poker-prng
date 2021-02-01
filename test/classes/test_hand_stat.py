#!/usr/bin/env python

import unittest

from classes import HandStat


class TestHandStat(unittest.TestCase):

    def setUp(self):
        self.hand_stat = HandStat.HandStat(9, 'Royal Straight Flush')

    def tearDown(self):
        del self.hand_stat
        HandStat.HandStat.hands_dealt = 0

    def test_increment_pass(self):
        self.hand_stat.increment()
        self.assertEqual(self.hand_stat.hits, 1)
        self.assertEqual(HandStat.HandStat.hands_dealt, 1)
        self.hand_stat.increment()
        self.assertEqual(self.hand_stat.hits, 2)
        self.assertEqual(HandStat.HandStat.hands_dealt, 2)

    def test_current_prob(self):
        self.hand_stat.increment()
        HandStat.HandStat.hands_dealt = 10
        self.assertEqual(self.hand_stat.current_prob(), 0.1)

    def test_ideal_prob(self):
        self.assertEqual(self.hand_stat.ideal_prob(), 0.00000154)


if __name__ == '__main__':
    unittest.main()
