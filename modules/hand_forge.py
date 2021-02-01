#!/usr/bin/env python

import os

from classes import Hand


'''
Module used for creating permutations of Hands.
'''
def create_hand_permutations(hand_string):
    '''
    Creates all the permutations of 5-card hands from a string representation
    of playing cards.
    
    Parameters:
        hand_string  (str):  string representation of playing cards.
                             Format is Rank + Suit (e.g. "2c 3d 4h 5s 6c").
    
    Returns:
        Hand: the new Hand object.
    '''
    hand_permutations = []
    card_string_array = hand_string.split(' ')
    if(len(card_string_array) == 7):
        for i in range(0, len(card_string_array) - 2):
            for j in range(i + 1, len(card_string_array) - 1):
                for k in range(j + 1, len(card_string_array) - 0):
                    for m in range(k + 1, len(card_string_array) - 0):
                        for n in range(m + 1, len(card_string_array) - 0):
                            hand_combination = [card_string_array[i],
                                                card_string_array[j],
                                                card_string_array[k],
                                                card_string_array[m],
                                                card_string_array[n]]
                            hand = Hand.Hand.parse_str(' '.join(hand_combination))
                            hand_permutations.append(hand)
    else:
        print('ERROR: Invalid card input, please try again. Program will now exit.')
        raise SystemExit
    return tuple(hand_permutations)
