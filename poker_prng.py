#!/usr/bin/env python

'''
Filename: poker_prng.py
Author: nlo
Python Version: 3.8.5

This is the main driver for the Poker PRNG tester.
This script can be run from the command line with
no arguments and will run on its own.
'''

import curses
import math
import sys
import time

from classes import Card
from classes import Deck
from classes import Hand
from classes import HandEval
from classes import HandStat
from classes import ScoreCard
from modules import hand_forge


# Rate for outputting stats to screen. Must be positive integer/float.
POLL_RATE = abs(0.1)


def output(screen, hand_stats, khps):
    '''
    Outputs the current hand statistics to the screen in real-time via curses.
    
    Parameters:
        hand_stats  (list[HandStat]):  contains HandStat data to display.
        khps        (float):           number of hands dealt and evaluated per second in thousands (kilo hands per second).
    '''
    screen.erase()
    total_percent = 0.0
    screen.addstr("       Hand Type      -   Current  |  Target   |   (+/-)\n")
    screen.addstr("------------------------------------------------------------\n")
    for hand_stat in hand_stats:
        total_percent += hand_stat.ideal_prob()
        screen.addstr(str(hand_stat) + "\n")
    screen.addstr("               Total  -  {}%\n".format(round(total_percent * 100, 2)))
    screen.addstr("------------------------------------------------------------\n")
    screen.addstr("\nHands Dealt: {}  @  {}k hands per second\n".format(HandStat.HandStat.hands_dealt,
                                                                        khps))
    screen.refresh()


def main():
    '''
    Main driver for the program - creates the hands and evaluates them as it outputs the results.
    
    Parameters:
        None
    '''
    screen = curses.initscr()
    hand_eval = HandEval.HandEval()
    hand_stats = [
        HandStat.HandStat(0, 'High Card'),
        HandStat.HandStat(1, 'Pair'),
        HandStat.HandStat(2, 'Two Pair'),
        HandStat.HandStat(3, 'Three of a Kind'),
        HandStat.HandStat(4, 'Straight'),
        HandStat.HandStat(5, 'Flush'),
        HandStat.HandStat(6, 'Full House'),
        HandStat.HandStat(7, 'Four of a Kind'),
        HandStat.HandStat(8, 'Straight Flush'),
        HandStat.HandStat(9, 'Royal Straight Flush')
    ]

    try:
        khps = 0
        count = 0
        before = time.time()
        output(screen, hand_stats, khps)
        while True:
            if time.time() - before >= POLL_RATE:
                if POLL_RATE < 1:
                  khps = round((count * (1 / POLL_RATE)) / 1000, 1)
                else:
                  khps = round((count / POLL_RATE) / 1000, 1)
                before = time.time()
                count = 0
                output(screen, hand_stats, khps)
            
            deck = Deck.Deck().new().shuffle()
            hand = deck.deal_cards(5)
            score_card = hand_eval.evaluate_hand(hand)
            hand_stat = hand_stats[score_card.hand_rank].increment()
            count += 1
    except KeyboardInterrupt as e:
        pass
    finally:
        screen.endwin()


if __name__ == '__main__':
    main()
