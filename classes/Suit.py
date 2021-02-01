#!/usr/bin/env python


class Suit(object):
    '''
    Class used for representing the suit of a playing card.
    
    Attributes:
        suit     (Suit):  the suit of the instance.
        CLUB     (Suit):  represents a Club suit.
        DIAMOND  (Suit):  represents a Diamond suit.
        HEART    (Suit):  represents a Heart suit.
        SPADE    (Suit):  represents a Spade suit.
    '''
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3

    def __init__ (self, suit):
        '''
        Class constructor.
        
        Parameters:
            suit  (str):  case-insensitive string representation of the suit: C, D, H, S.
        '''
        suit = suit.upper()
        if suit == 'C':
            self.suit = Suit.CLUB
        elif suit == 'D':
            self.suit = Suit.DIAMOND
        elif suit == 'H':
            self.suit = Suit.HEART
        else:
            self.suit = Suit.SPADE

    def __lt__ (self, suit):
        '''
        Less-Than comparison override for the class.
        Suit order value in ascending order CLUB < DIAMOND < HEART < SPADE.
        
        Parameters:
            suit  (Suit):  suit to be compared against.
        
        Returns:
            bool: true if self is less-than in value to other suit.
        '''
        return self.suit < suit

    def __gt__(self, suit):
        '''
        Greater-Than comparison override for the class.
        Suit order value in ascending order SPADE > HEART > DIAMOND > CLUB.
        
        Parameters:
            suit  (Suit):  suit to be compared against.
        
        Returns:
            bool: true if self is greater-than in value to other suit.
        '''
        return self.suit > suit

    def __eq__(self, suit):
        '''
        Equality comparison override for the class.
        
        Parameters:
            suit  (Suit):  suit to be compared against.
        
        Returns:
            bool: true if self is equal in value to other suit.
        '''
        return self.suit == suit

    def __str__(self):
        '''
        String override for the class.
        
        Parameters:
            None
        
        Returns:
            str: unicode string of the suit.
        '''
        if(self.suit == Suit.CLUB):
            return u'\u2663'
        elif(self.suit == Suit.DIAMOND):
            return u'\u2666'
        elif(self.suit == Suit.HEART):
            return u'\u2665'
        return u'\u2660'

    def print_alpha(self):
        '''
        Print regular alpha characters for suits.
        
        Parameters:
            None
        
        Returns:
            str: alpha characters of the suit.
        '''
        if(self.suit == Suit.CLUB):
            return 'C'
        elif(self.suit == Suit.DIAMOND):
            return 'D'
        elif(self.suit == Suit.HEART):
            return 'H'
        return 'S'
