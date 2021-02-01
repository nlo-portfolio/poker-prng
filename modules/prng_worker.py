#!/usr/bin/env python

from classes import Deck
from classes import HandEval


'''
Worker thread for evaluating poker hands.
'''
def run(queue_out):
    hand_eval = HandEval.HandEval()
    deck = Deck.Deck()
    while True:
        deck.new().shuffle()
        hand = deck.deal_cards(5)
        score_card = hand_eval.evaluate_hand(hand)
        queue_out.put(score_card.hand_rank)
