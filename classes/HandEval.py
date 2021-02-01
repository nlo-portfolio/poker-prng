#!/usr/bin/env python

from . import ScoreCard
from . import Hand


class HandEval:
    '''
    Class used for evaluating hands of playing cards for matches to common hands
    and returns the first highest-ranked match.
    
    Attributes:
        rank_histogram  (list):  contains a count of all ranks in the hand.
        suit_histogram  (list):  contains a count of all suits in the hand.
    '''
    rank_histogram = []
    suit_histogram = []

    def __init__(self):
        '''
        Default constructor.
        '''
        pass

    def evaluate_hand(self, hand):
        '''
        Evaluates a single hand in descending order of rank and returns the first match.
        
        Parameters:
            hand  (Hand):  the hand to be evaluated.
        
        Returns:
            ScoreCard: contains the result of the evaluation.
        '''
        HandEval.rank_histogram = hand.get_rank_histogram()
        HandEval.suit_histogram = hand.get_suit_histogram()

        hand = hand.sort(reverse=True)
        result = self.is_royal_straight_flush(hand)
        if result: return ScoreCard.ScoreCard(result, 9)

        result = self.is_straight_flush(hand)
        if result: return ScoreCard.ScoreCard(result, 8)

        result = self.is_four_of_kind(hand)
        if result: return ScoreCard.ScoreCard(result, 7)

        result = self.is_full_house(hand)
        if result: return ScoreCard.ScoreCard(result, 6)

        result = self.is_flush(hand)
        if result: return ScoreCard.ScoreCard(result, 5)

        result = self.is_straight(hand)
        if result: return ScoreCard.ScoreCard(result, 4)

        result = self.is_three_of_kind(hand)
        if result: return ScoreCard.ScoreCard(result, 3)

        result = self.is_two_pair(hand)
        if result: return ScoreCard.ScoreCard(result, 2)

        result = self.is_pair(hand)
        if result: return ScoreCard.ScoreCard(result, 1)

        return ScoreCard.ScoreCard(hand, 0)

    def is_royal_straight_flush(self, hand):
        '''
        Evaluates a hand for a Royal Straight Flush.
        
        Parameters:
            hand  (Hand):  hand to be evaluated.
        
        Returns:
            Hand: sorted hand if match, none if no match.
        '''
        if self.is_straight_flush(hand):
            if(HandEval.rank_histogram[len(HandEval.rank_histogram) - 1] > 0):
                return hand
        return None

    def is_straight_flush(self, hand):
        '''
        Evaluates a hand for a Straight Flush.
        
        Parameters:
            hand  (Hand):  hand to be evaluated.
        
        Returns:
            Hand: sorted hand if match, None if no match.
        '''
        if self.is_straight(hand) and self.is_flush(hand):
            return hand
        return None

    def is_four_of_kind(self, hand):
        '''
        Evaluates a hand for a Four of a Kind.
        
        Parameters:
            hand  (Hand):  hand to be evaluated.
        
        Returns:
            Hand: sorted hand if match, none if no match.
        '''
        if 4 in HandEval.rank_histogram:
            return hand.float_ranks(HandEval.rank_histogram.index(4) + 2)
        return None

    def is_full_house(self, hand):
        '''
        Evaluates a hand for a Full House.
        
        Parameters:
            hand  (Hand):  hand to be evaluated.
        
        Returns:
            Hand: sorted hand if match, none if no match.
        '''
        if (2 in HandEval.rank_histogram) and (3 in HandEval.rank_histogram):
            return hand
        return None

    def is_flush(self, hand):
        '''
        Evaluates a hand for a Flush.
        
        Parameters:
            hand  (Hand):  hand to be evaluated.
        
        Returns:
            Hand: sorted hand if match, none if no match.
        '''
        if 5 in HandEval.suit_histogram:
            return hand
        return None

    def is_straight(self, hand):
        '''
        Evaluates a hand for a Straight (including Ace-low).
        
        Parameters:
            hand  (Hand):  hand to be evaluated.
        
        Returns:
            Hand: sorted hand if match, none if no match.
        '''
        for i in range(len(HandEval.rank_histogram) - 1, 3, -1):
            if((HandEval.rank_histogram[i] == 1) and
               (HandEval.rank_histogram[i - 1] == 1) and
               (HandEval.rank_histogram[i - 2] == 1) and
               (HandEval.rank_histogram[i - 3] == 1) and
               (HandEval.rank_histogram[i - 4] == 1)):
                   return hand

        # Evaluate Ace-low straight.
        if ((HandEval.rank_histogram[12] == 1) and
            (HandEval.rank_histogram[0] == 1) and
            (HandEval.rank_histogram[1] == 1) and
            (HandEval.rank_histogram[2] == 1) and
            (HandEval.rank_histogram[3] == 1)):
                return hand
        return None

    def is_three_of_kind(self, hand):
        '''
        Evaluates a hand for a Three of a Kind.
        
        Parameters:
            hand  (Hand):  hand to be evaluated.
        
        Returns:
            Hand: sorted hand if match, none if no match.
        '''
        if 3 in HandEval.rank_histogram:
            return hand.float_ranks(HandEval.rank_histogram.index(3) + 2)
        return None

    def is_two_pair(self, hand):
        '''
        Evaluates a hand for a Two-Pair.
        
        Parameters:
            hand  (Hand):  hand to be evaluated.
        
        Returns:
            Hand: sorted hand if match, none if no match.
        '''
        if HandEval.rank_histogram.count(2) == 2:
            for i in range(len(HandEval.rank_histogram) - 1):
                if HandEval.rank_histogram[i] == 2:
                    hand.float_ranks(i + 2)
            return hand
        return None

    def is_pair(self, hand):
        '''
        Evaluates a hand for a Pair.
        
        Parameters:
            hand  (Hand):  hand to be evaluated.
        
        Returns:
            Hand: sorted hand if match, none if no match.
        '''
        if 2 in HandEval.rank_histogram:
            return hand.float_ranks(HandEval.rank_histogram.index(2) + 2)
        return None
