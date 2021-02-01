#!/usr/bin/env python

import re

from . import Suit
from . import Rank


class Card(object):
    '''
    Class used to represent a playing card with suit and rank.
    
    Attributes:
        rank  (Rank object):  valid ranks include 2-10,J,Q,K,A.
        suit  (Suit object):  valid suits include C,D,H,S.
    '''
    def __init__ (self, rank, suit):
        '''
        Class constructor.
        
        Parameters:
            rank  (int):  the rank as an integer.
            suit  (str):  the suit as a string.
        '''
        self.rank = Rank.Rank(rank)
        self.suit = Suit.Suit(suit)

    @classmethod
    def new(cls, card_code):
        '''
        Secondary constructor suited for user input strings.
        
        Parameters:
            card_code  (str):  string representing rank and suit.
        '''
        match = re.match("(([2-9]{1})|10|([jqkaJQKA]{1}))[cdhsCDHS]{1}", card_code)
        if match == None:
            return None

        rank = re.match("[2-9]{1}|10|[jqkaJQKA]{1}", match[0])[0]
        try:
            rank = int(rank)
        except ValueError:
            if rank.upper() == 'J':
               rank = 11
            elif rank.upper() == 'Q':
               rank = 12
            elif rank.upper() == 'K':
               rank = 13
            elif rank.upper() == 'A':
               rank = 14
        suit = re.search("[cdhsCDHS]{1}", match[0])[0]
        return Card(rank, suit)

    def __lt__(self, card):
        '''
        Less-Than comparison override for the class.
        Suit order value in ascending order CLUB < DIAMOND < HEART < SPADE.
        
        Parameters:
            card  (Card):  card to be compared against.
        
        Returns:
            bool: true if self is less-than in value to other card.
        '''
        if self.rank == card.rank:
            return self.suit < card.suit
        return self.rank < card.rank

    def __gt__(self, card):
        '''
        Greater-Than comparison override for the class.
        Suit order value in ascending order SPADE > HEART > DIAMOND > CLUB.
        
        Parameters:
            card  (Card):  card to be compared against.
        
        Returns:
            bool: true if self is greater-than in value to other card.
        '''
        if self.rank == card.rank:
            return self.suit > card.suit
        return self.rank > card.rank

    def __eq__(self, card):
        '''
        Equality comparison override for the class.
        
        Parameters:
            card  (Card):  card to be compared against.
        
        Returns:
            bool: true if self is equal in value to other card.
        '''
        if self.rank == card.rank:
            return self.suit == card.suit
        return self.rank == card.rank

    def __str__(self):
        '''
        String override for the class.
        
        Parameters:
            None
            
        Returns:
            str: string representation of the card.
        '''
        return (str(self.rank) + str(self.suit))

    def print_alpha(self):
        '''
        Print regular alpha characters for suits.
        
        Parameters:
            None
        
        Returns:
            str: alpha characters of the suit.
        '''
        return (str(self.rank) + self.suit.print_alpha())
