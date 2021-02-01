#!/usr/bin/env python

import re


class Rank(object):
    '''
    Class used for representing the rank of a playing card.
    
    Attributes:
        rank  (int):  rank value in ascending order.
    '''
    def __init__(self, rank):
        '''
        Class constructor.
        
        Parameters:
            rank  (int):  rank value in ascending order.
        '''
        self.rank = rank

    @classmethod
    def new(cls, rank_str):
        '''
        Secondary constructor suited for user input strings.
        
        Parameters:
            rank_str  (str):  rank value in ascending order.
        '''
        rank = None
        try:
            rank = re.match("[2-9]{1}|10", rank_str)[0]
        except TypeError:
            rank = re.match("[jqkaJQKA]{1}", rank_str)[0]
            if rank.upper() == 'J':
                rank = 11
            elif rank.upper() == 'Q':
                rank = 12
            elif rank.upper() == 'K':
                rank = 13
            else:
                rank = 14
        finally:
            self.rank = int(rank)

    def __lt__ (self, rank):
        '''
        Less-Than comparison override for the class.
        
        Parameters:
            rank  (Rank):  rank to be compared against.
        
        Returns:
            bool: true if self is less-than in value to other rank.
        '''
        return self.rank < rank.rank

    def __gt__(self, rank):
        '''
        Greater-Than comparison override for the class.
        
        Parameters:
            rank  (Rank):  rank to be compared against.
        
        Returns:
            bool: true if self is greater-than in value to other rank.
        '''
        return self.rank > rank.rank

    def __eq__(self, rank):
        '''
        Equality comparison override for the class.
        
        Parameters:
            rank  (Rank):  rank to be compared against.
        
        Returns:
            bool: true if self is equal in value to other rank.
        '''
        return self.rank == rank

    def __str__(self):
        '''
        String override for the class.
        
        Parameters:
            None
            
        Returns:
            str: string representation of the rank.
        '''
        if self.rank < 11:
            return str(self.rank)

        if self.rank == 11:
            return 'J'
        if self.rank == 12:
            return 'Q'
        if self.rank == 13:
            return 'K'
        return 'A'
