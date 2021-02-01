#!/usr/bin/env python

import unittest

from classes import Card
from classes import Deck
from classes import Suit


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck.Deck()

    def tearDown(self):
        pass

    def test_new_deck_pass(self):
        self.assertFalse(self.deck.deck)
        self.deck = self.deck.new()
        self.assertEqual(len(self.deck.deck), 52)

    def test_deal_card_pass(self):
        self.deck.new()
        card = self.deck.deal_card()
        self.assertEqual(card.rank.rank, 14)
        self.assertEqual(card.suit.suit, Suit.Suit.HEART)

    def test_deal_cards_pass(self):
        self.deck.new()
        hand = self.deck.deal_cards(7)
        self.assertEqual(hand.hand[0].rank.rank, 14)
        self.assertEqual(hand.hand[0].suit.suit, Suit.Suit.HEART)
        self.assertEqual(hand.hand[1].rank.rank, 2)
        self.assertEqual(hand.hand[1].suit.suit, Suit.Suit.HEART)
        self.assertEqual(hand.hand[2].rank.rank, 3)
        self.assertEqual(hand.hand[2].suit.suit, Suit.Suit.HEART)
        self.assertEqual(hand.hand[3].rank.rank, 4)
        self.assertEqual(hand.hand[3].suit.suit, Suit.Suit.HEART)
        self.assertEqual(hand.hand[4].rank.rank, 5)
        self.assertEqual(hand.hand[4].suit.suit, Suit.Suit.HEART)
        self.assertEqual(hand.hand[5].rank.rank, 6)
        self.assertEqual(hand.hand[5].suit.suit, Suit.Suit.HEART)
        self.assertEqual(hand.hand[6].rank.rank, 7)
        self.assertEqual(hand.hand[6].suit.suit, Suit.Suit.HEART)

    def test_shuffle_pass(self):
        self.deck.new()
        new_deck = Deck.Deck().new()
        self.assertEqual(new_deck.deck, self.deck.deck)
        self.deck.new().shuffle()
        self.assertNotEqual(new_deck.deck, self.deck.deck)


if __name__ == '__main__':
    unittest.main()
