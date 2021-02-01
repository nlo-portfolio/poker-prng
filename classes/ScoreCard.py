#!/usr/bin/env python

import os


class ScoreCard(object):
    '''
    Class used for tracking the results of hand evaluations.

    Note that the 64-bit score is designed to be compared against other
    hands. First, the hand type is assigned a value between 0 and 9.
    Second, the most valuable cards in the hand are sorted in descending
    order, followed by the non-hand related cards. Third, the cards are
    assigned numerical values (2 = 02, J = 11, A = 14) and appended to
    the overall hand ranking value. A sample score for the hand:
        2h 3h 4h 5h 6h = 90203040506 = Straight Flush
        2c 2d 2h 2s 3h = 70202020203 = Four of a Kind
    
    Attributes:
        hand_strings  (dict):  contains the English names for all hands.
        hand          (Hand):  the hand to be scored.
        score         (str):   the calculated integer score value as a string.
    '''
    hand_strings = {
        0: 'High Card',
        1: 'Pair',
        2: 'Two-Pair',
        3: 'Three of a Kind',
        4: 'Straight',
        5: 'Flush',
        6: 'Full House',
        7: 'Four of a Kind',
        8: 'Straight Flush',
        9: 'Royal Straight Flush'
    }

    def __init__(self, hand, hand_rank):
        '''
        Class constructor.
        
        Parameters:
            hand       (Hand):  the hand to be scored.
            hand_rank  (int):   id/rank of the hand in ascending order.
        '''
        if hand is None or hand_rank is None:
            self.hand = None
            self.hand_rank = None
            self.score = 0
        else:
            self.hand = hand
            self.hand_rank = hand_rank
            self.score = self.calc_score()

    def calc_score(self):
        '''
        Calculates the score of a winning hand based on card value (both rank and suit).
        Multiplies values out for exponentially for easier visual separation of results.
        Returns result as a string to bypass integer limitations on different platforms.
        
        Parameters:
            None
        
        Returns:
            str: integer score of the hand as a string.
        '''
        score_sum = self.hand_rank * 10000000000
        score_sum += self.hand.hand[0].rank.rank * 100000000
        score_sum += self.hand.hand[1].rank.rank * 1000000
        score_sum += self.hand.hand[2].rank.rank * 10000
        score_sum += self.hand.hand[3].rank.rank * 100
        score_sum += self.hand.hand[4].rank.rank * 1
        return str(score_sum)

    def hand_str(self):
        '''
        Returns the English name of the hand based on its rank.
        
        Parameters:
            None
        
        Returns:
            str: english name of the hand.
        '''
        return ScoreCard.hand_strings[self.hand_rank]

    def __lt__(self, score_card):
        '''
        Less-Than comparison override for the class.
        
        Parameters:
            score_card  (ScoreCard):  score card to be compared against.
        
        Returns:
            bool: true if self is less-than in value to other score card.
        '''
        if self.hand_rank == score_card.hand_rank:
            return self.score < score_card.score
        return self.hand_rank < score_card.hand_rank

    def __gt__(self, score_card):
        '''
        Greater-Than comparison override for the class.
        
        Parameters:
            score_card  (ScoreCard):  score card to be compared against.
        
        Returns:
            bool: true if self is greater-than in value to other score card.
        '''
        if self.hand_rank == score_card.hand_rank:
            return self.score > score_card.score
        return self.hand_rank > score_card.hand_rank

    def __eq__(self, score_card):
        '''
        Equality comparison override for the class.
        
        Parameters:
            score_card  (ScoreCard):  score card to be compared against.
        
        Returns:
            bool: true if self is equal in value to other score card.
        '''
        if self.hand_rank == score_card.hand_rank:
            return self.score == score_card.score
        return self.hand_rank == score_card.hand_rank

    def __str__(self):
        '''
        String override for the class.
        
        Parameters:
            None
        
        Returns:
            str: string representation of the object.
        '''
        hand_str = self.hand_str()
        return (
            'YOUR HAND: ' + str(self.hand) + ' -  RESULT: Hand is a ' +
            self.hand_str() + '  -  SCORE: ' + self.score + os.linesep
        )
