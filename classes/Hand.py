#!/usr/bin/env python

import re

from . import Card
from . import Suit


class Hand(object):
    '''
    Class used for representing a single hand of cards.
    
    Attributes:
        hand  (tuple):  holds the cards for the hand.
    '''
    def __init__(self, card_list):
        '''
        Class constructor.
        
        Parameters:
            card_list  (list):  list containing Card objects.
        '''
        self.hand = tuple(card_list)

    @classmethod
    def parse_str(cls, hand_string):
        '''
        Class method for parsing a string and returning of a hand of playing cards.
        
        Parameters:
            hand  (str):  string representation of playing cards.
                          Format is Rank + Suit (e.g. "2c 3d 4h 5s 6c").
        
        Returns:
            Hand: the new hand.
        '''
        card_list = []
        hand_string_array = hand_string.split(' ')
        for card in hand_string_array:
            card_list.append(Card.Card.new(card))
        return Hand(card_list)

    @classmethod
    def validate(cls, input_cards, num_cards):
        '''
        Ensures that the input string matches the expected format, minimum number of cards and
        that there are no duplicates. NOTE: Will match and return the first n cards it encounters.
        
        Parameters:
            input_cards  (str):  string of card codes.
        
        Returns:
            bool: true if valid, false if invalid.
        '''
        # Regex does not like multi-line triple-quoted strings - leave as-is.
        pattern = "^((([2-9]|[10]\d|[jqkaJQKA])[cdhsCDHS])\s{{1,}}?){{{}}}?(([2-9]|[10]\d|[jqkaJQKA])[cdhsCDHS]){{1}}?$".format(num_cards - 1)
        regex = re.compile(pattern)
        regex_result = regex.match(input_cards)
        if not regex_result:
            return False

        # Check for duplicate cards.
        card_array = input_cards.split()
        for card_one in range(len(card_array) - 1):
            for card_two in range(card_one + 1, len(card_array)):
                if card_array[card_one].upper() == card_array[card_two].upper():
                    return False
        return True

    def get_rank_histogram(self):
        '''
        Creates and returns a histogram (as a list) indicating the counts of particular ranks.
        
        Parameters:
            None
        
        Returns:
            list: histogram as a list of rank counts.
        '''
        rank_count = [0] * 13
        for i in range(0, len(self.hand)):
            rank_count[self.hand[i].rank.rank - 2] += 1
        return rank_count

    def get_suit_histogram(self):
        '''
        Creates and returns a histogram (as a list) indicating the counts of particular suits.
        
        Parameters:
            None
        
        Returns:
            list: histogram as a list of suit counts.
        '''
        suit_count = [0] * 4
        for card in self.hand:
            suit_count[card.suit.suit] += 1
        return suit_count

    def get_list(self):
        '''
        Returns the hand as a list.
        
        Parameters:
            None
        
        Returns:
            list: The cards from the hand.
        '''
        return list(self.hand)
        
    def float_ranks(self, rank):
        '''
        Shift cards of the specified rank to the front of the hand.
        
        Parameters:
            int: rank to be shifted.
            
        Returns:
            Hand: self
        '''
        t = list(self.hand)
        for card in t:
            if card.rank.rank == rank:
                t.insert(0, t.pop(t.index(card)))
        self.hand = tuple(t)
        return self

    def sort(self, reverse=False):
        '''
        Sorts the cards in ascending order (lowest rank and suit first).
        
        Parameters:
            None
        
        Returns:
            Hand: the sorted hand.
        '''
        temp_list = list(self.hand)
        temp_list.sort(reverse=reverse)
        self.hand = tuple(temp_list)
        return self

    def __str__(self):
        '''
        String override for the class.
        
        Parameters:
            None
        
        Returns:
            str: hand cards as a string separated by a space.
        '''
        s = ''
        for card in self.hand:
            s += str(card) + ' '
        return s

    def print_alpha(self):
        '''
        Print regular alpha characters for suits.
        
        Parameters:
            None
        
        Returns:
            str: alpha characters of the suit.
        '''
        return ' '.join(card.print_alpha() for card in self.hand)
