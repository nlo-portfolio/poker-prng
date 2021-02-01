#!/usr/bin/env python


class HandStat(object):
    '''
    Class used for tracking statistics on dealt hands.
    
    Attributes:
        hands_dealt  (int):   total number of hands dealt.
        ideal_probs  (dict):  contains the ideal probabilities for all hands.
        hand_rank    (int):   id/rank of the hand in ascending order.
        hand_name    (str):   english name of the known hand.
        hits         (int):   count for the number of hand occurrence.
    '''
    hands_dealt = 0
    ideal_probs = {
        0: 0.501177,
        1: 0.422569,
        2: 0.047539,
        3: 0.021128,
        4: 0.003925,
        5: 0.001965,
        6: 0.001441,
        7: 0.000240,
        8: 0.0000139,
        9: 0.00000154
    }

    def __init__(self, hand_rank, hand_name):
        '''
        Class constructor.
        
        Parameters:
            hand_rank  (int):  id/rank of the hand in ascending order.
            hand_name  (str):  english name of the known hand.
        '''
        self.hand_rank = hand_rank
        self.hand_name = hand_name
        self.hits = 0

    def increment(self):
        '''
        Increments the total hands dealt for the class and number of hits for the instance.
        
        Parameters:
            None
        '''
        self.hits += 1
        HandStat.hands_dealt += 1

    def current_prob(self):
        '''
        Calculates the current probability (so far) of each hand in retrospect.
        
        Parameters:
            None
        
        Returns:
            float: current probability.
        '''
        if HandStat.hands_dealt == 0:
            return 0.0
        return float(self.hits / HandStat.hands_dealt)

    def ideal_prob(self):
        '''
        The ideal probability of the Poker hand.
        
        Parameters:
            None
        
        Returns:
            float: ideal probability.
        '''
        return HandStat.ideal_probs[self.hand_rank]

    def __str__(self):
        '''
        String override for the class.
        
        Parameters:
            None
        
        Returns:
            str: string representation of the object.
        '''
        spacing = ' ' * (20 - len(self.hand_name))
        current_prob = self.current_prob()
        ideal_prob = self.ideal_prob()
        return "{}{}  -  {}% | {}% | {}%".format(self.hand_name, spacing,
                                           str(round(current_prob * 100, 5)).ljust(8, '0'),
                                           str(round(ideal_prob * 100, 5)).ljust(8, '0'),
                                           str(round(abs(current_prob - ideal_prob) * 100, 5)).ljust(8, '0'))
