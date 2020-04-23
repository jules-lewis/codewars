"""
Ranking Poker Hands

URL: https://www.codewars.com/kata/5739174624fc28e188000465/train/python

A famous casino is suddenly faced with a sharp decline of their revenues. 
They decide to offer Texas hold'em also online. Can you help them by 
writing an algorithm that can rank poker hands?

Task

Create a poker hand that has a method to compare itself to another poker 
hand:

    compare_with(self, other_hand)

A poker hand has a constructor that accepts a string containing 5 cards:

    PokerHand("KS 2H 5C JD TD")

The characteristics of the string of cards are:

Each card consists of two characters, where

    The first character is the value of the card: 2, 3, 4, 5, 6, 7, 8, 9, 
    T(en), J(ack), Q(ueen), K(ing), A(ce)

    The second character represents the suit: S(pades), H(earts), D(iamonds), 
    C(lubs)

    A space is used as card separator between cards

The result of your poker hand compare can be one of these 3 options:

    [ "Win", "Tie", "Loss" ]

Notes

Apply the Texas Hold'em rules for ranking the cards
[ https://en.wikipedia.org/wiki/Texas_hold_%27em#Hand_values ]

Low aces are NOT valid in this kata.

There is no ranking for the suits.

(1) First things first: have I written this before? It turns out 
    this is very similar to Euler Problem 54, which I completed 
    in 2017. In this problem, the hands are scored 1 to 10, with 
    1 being the lowest ranked hand (High Card) and 10 being the 
    highest ranked hand (Royal Flush). However, Royal Flush could 
    be considered the same thing as a stright flush, but with a
    better high card, so I will only rank hands 1-9.

    The Euler code was written as functions, so implementing
    PokerHand as a class will be new for me.

(2) It looks like compare_with() is using a hand (i.e. string)
    for other, so this is how I'll implement it for now. The 
    alternative is that it is a PokerHand, but I guess we'll see.

(3) Running the code in CodeWars, it seems that compare_with() takes
    another PokerHand as the second parameter.

"""

class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        
        #Let's divide the cards up first
        cards = hand.split()
        #Then sort them in descending order. The addition of '0'
        # and '1' means that each card gets assigned its correct 
        # ordinal, e.g. 'K' = 13.
        self._ranks = sorted(['0123456789TJQKA'.find(c) for c, s in cards], reverse = True)
        
        #Store the suits also (which only really matter in flushes)
        self._suits = [s for c, s in cards]


    def __of_a_kind(self, ranks, num):
        """ Will check for "num of a kind" ranks in a hand (e.g. "three of a
        kind") and if found, will return the cards sorted with the 'of a kind' 
        first, then the rest sorted in reverse order. The easiest way to see 
        the outcome of this is if you passed in the ranks [K, J, J, J, 9] 
        and asked it to check for three of a kind. The list you would get 
        back would be the three Jacks, followed by the remainder of the
        ranks in reverse order, i.e.: [J, J, J, K, 9]. The reason for this 
        is so that you can use one function for checking all the 'of a kind'
        hands, while also being able to compare hands with single and double 
        pairs, along with Full House. """
        for i in range(14, 0, -1):
            if ranks.count(i) == num:
                return [i]*num + sorted([c for c in ranks if c != i], reverse = True)
        return 0

    def get_score(self):

        #shorthand
        r = self._ranks
        s = self._suits

        b_flush = len(set(s)) == 1

        #Is it a STRAIGHT? The test for this is:
        # - is the difference between the top rank and
        #   the bottom rank = 4
        #    _ AND _
        # - are all five ranks different?!
        if (r[0]-r[4]==4) and (len(set(r))==5):
            
            #Is it a STRAIGHT FLUSH?
            if b_flush:
                return [9] + r
            else:
                return [5] + r

        #Is it just a FLUSH?
        if b_flush: return [6] + r

        #Is it FOUR OF A KIND?
        rtn = self.__of_a_kind(r, 4)
        if rtn: return [8] + rtn

        #Is there a THREE OF A KIND?
        rtn = self.__of_a_kind(r, 3)
        if rtn:
            #If so, is it a FULL HOUSE?
            rtn2 = self.__of_a_kind(rtn[3:], 2)
            if rtn2:
                return [7] + rtn[0:3] + rtn2
            else:
                return [4] + rtn

        #Have we got a PAIR at least??
        rtn = self.__of_a_kind(r, 2)
        if rtn:
            #TWO PAIR?
            rtn2 = self.__of_a_kind(rtn[2:], 2)
            if rtn2:
                return [3] + rtn[0:2] + rtn2
            else:
                return [2] + rtn

        #TOP CARD...
        return [1] + r

    def compare_with(self, other):

        score1 = self.get_score()
        score2 = other.get_score()
        if score1 > score2:
            rtn = 2
        elif score1 < score2:
            rtn = 0
        else:
            rtn = 1

        return self.RESULT[rtn]


def test_hand(str_cards):
    test_poker_hand = PokerHand(str_cards)
    print(test_poker_hand.get_score())
    cw1 = PokerHand("2H 3H 4S 5D 6H")
    cw2 = PokerHand("2S 5H 6H AS QC")
    print(test_poker_hand.compare_with(cw1))
    print(test_poker_hand.compare_with(cw2))

test_hand("2H 3H 4H 5H 6H")      # Straight flush               = 9   
test_hand("KS AS TS QS JS")      # Royal Flush (straight flush) = 9
test_hand("AS AD AC AH JD")      # Four of a kind               = 8
test_hand("AS AH 5H 5C AC")      # Full House                   = 7
test_hand("2S 7S 4S KS AS")      # Flush                        = 6
test_hand("2H 3H 4S 5D 6H")      # Straight                     = 5
test_hand("AS 2H AD 5C AC")      # Three of a kind              = 4
test_hand("AS 2H 5C 2D AC")      # Two pair                     = 3
test_hand("AS 3H 5C 2D AC")      # Pair                         = 2
test_hand("2S 5H 6H AS QC")      # Top                          = 1


