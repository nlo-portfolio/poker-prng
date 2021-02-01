#!/usr/bin/env python

'''
Filename: python_poker.py
Author: nlo
Python Version: 3.8.5

This is the main driver for the Python Poker hand evaluator.
Run this module with no arguments and follow the command-line prompts.
'''

import os
import re

from classes import Hand
from classes import ScoreCard
from modules import poker_game


def main():
    '''
    Main driver for the program - requests input from the user including type of poker game to play and
    the cards to evaluate.
    
    Parameters:
        None
    '''
    while True:
        score_card = None
        print('Please enter 5 or 7 cards (Example: "2c 3d 4h 5s 6c" or "2h 4c 10c jd qh ks ac" with no quotes): ')
        input_cards = input()
        if Hand.Hand.validate(input_cards, 5):
            score_card = poker_game.run_game_five_card_draw(input_cards)
        elif Hand.Hand.validate(input_cards, 7):
            score_card = poker_game.run_game_texas_hold_em(input_cards)

        if score_card:
            print(score_card)
        else:
            print('Error: Input invalid. Please check the format (no duplicates allowed) and try again.')


if __name__ == '__main__':
    main()
