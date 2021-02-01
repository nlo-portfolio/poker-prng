#!/usr/bin/env python

import secrets
import sys

from . import Card
from . import Hand


class Deck(object):
    '''
    Class used to represent a deck of standard playing cards.
    
    Attributes:
        deck  (list):  contains the list of cards.
    '''
    def __init__(self):
        '''
        Class constructor.
        '''
        self.deck = []

    def new(self):
        '''
        Creates a new deck of playing cards in standard New Deck Order (NDO).
        
        Parameters:
            None
            
        Returns:
            Deck: self.
        '''
        ranks = [14] + [ i for i in range(2, 14) ]

        suits_asc = ['S', 'D']
        self.deck = [
                        Card.Card(rank, suit)
                        for suit in suits_asc
                        for rank in ranks
                    ]

        suits_desc = ['C', 'H']
        ranks.reverse()
        self.deck += [
                         Card.Card(rank, suit)
                         for suit in suits_desc
                         for rank in ranks
                     ]

        return self

        '''
        for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            for suit in ['C', 'D', 'H', 'S']:
                self.deck.append(Card.Card(rank + suit))
        '''

    def deal_card(self):
        '''
        Deals a single card from the deck top of the deck.
        
        Parameters:
            None
        
        Returns:
            Card: the dealt card.
        '''
        return self.deck.pop()

    def deal_cards(self, num_cards=1):
        '''
        Deals a variable number of cards from the top of the deck.
        
        Parameters:
            num_cards  (int):  number of cards to be dealt.
            
        Returns:
            Hand: hand containing the dealt cards.
        '''
        if num_cards < 0 or num_cards > len(self.deck):
            raise ValueError

        cards = []
        for i in range(num_cards):
            cards.append(self.deck.pop())
        return Hand.Hand(cards)

    def shuffle(self):
        '''
        Shuffles the deck using the Fisher-Yates algorithm.
        
        Parameters:
            None
            
        Returns:
            Deck: self.
        '''
        for i in range(len(self.deck) - 1, 0, -1):
            j = secrets.randbelow(i + 1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
        return self

    def __str__(self):
        '''
        String override for the class.
        
        Parameters:
            None
        
        Returns:
            str: string representation of the deck of cards.
        '''
        str_list = []
        for card in self.deck:
            str_list.append(str(card))
        return str(str_list)
