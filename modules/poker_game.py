#!/usr/bin/env python

from classes import Hand
from classes import HandEval
from classes import ScoreCard
from modules import hand_forge


def run_game_five_card_draw(cards):
    '''
    Evaluates the passed cards as they would be in 5-Card Draw Poker.
    
    Parameters:
        cards  (str):  playing cards to be evaluated as a string.
    
    Returns:
        ScoreCard: contains the result of the hand evaluation.
    '''
    hand = Hand.Hand.parse_str(cards)
    hand_eval = HandEval.HandEval()
    return hand_eval.evaluate_hand(hand)


def run_game_texas_hold_em(cards):
    '''
    Evaluates the passed cards as they would be in Texas Hold 'Em Poker.
    7 playing cards are provided and all permutations are calculated, with the
    highest rated hand as winner.
    
    Parameters:
        cards  (str):  playing cards to be evaluated as a string.
    
    Returns:
        ScoreCard: contains the result of the hand evaluation.
    '''
    hand_eval = HandEval.HandEval()
    hand_permutations = hand_forge.create_hand_permutations(cards)
    best_score = ScoreCard.ScoreCard(None, None)
    for hand in hand_permutations:
        result = hand_eval.evaluate_hand(hand)
        if int(result.score) > int(best_score.score):
            best_score = result
    return best_score
