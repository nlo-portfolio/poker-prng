#!/usr/bin/env python

import unittest

from classes import Hand
from modules import hand_forge


class TestHandForge(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_hand_permutations(self):
        truth = [
            '8C 9D 10H JS QC',
            '8C 9D 10H JS KD',
            '8C 9D 10H JS AH',
            '8C 9D 10H QC KD',
            '8C 9D 10H QC AH',
            '8C 9D 10H KD AH',
            '8C 9D JS QC KD',
            '8C 9D JS QC AH',
            '8C 9D JS KD AH',
            '8C 9D QC KD AH',
            '8C 10H JS QC KD',
            '8C 10H JS QC AH',
            '8C 10H JS KD AH',
            '8C 10H QC KD AH',
            '8C JS QC KD AH',
            '9D 10H JS QC KD',
            '9D 10H JS QC AH',
            '9D 10H JS KD AH',
            '9D 10H QC KD AH',
            '9D JS QC KD AH',
            '10H JS QC KD AH'
        ]
        hand_permutations = hand_forge.create_hand_permutations('8c 9d 10h Js Qc Kd Ah')
        for i in range(len(hand_permutations) - 1):
            self.assertEqual(truth[i], hand_permutations[i].print_alpha())


if __name__ == '__main__':
    unittest.main()
