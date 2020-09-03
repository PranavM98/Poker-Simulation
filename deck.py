#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:06:59 2020

@author: pranavmanjunath
"""

from card import Card, card_from_num
import random


class Deck:
    ''' Class to define the Deck.'''

    def __init__(self):
        self.cards=[]
        pass
    def __str__(self):
        s=""
        for i in self.cards:
            if i ==self.cards[-1]:
                s=s+i.__str__()
            else:
                s=s+i.__str__()+" "
        return s    
    
    def __repr__(self):
        s="Deck("
        for i in self.cards:
            if i ==self.cards[-1]:
                s=s+i.__str__()
            else:
                s=s+i.__str__()+" "
        s=s+')'
        return s
        
    
    
    def add_card(self, c):
        self.cards.append(c)
        pass
    
    
    def add_empty_card(self):
        self.cards.append(Card('?','?'))
        return self.cards[-1]
        pass
    
    
    def contains(self, c):
        flag=0
        for i in self.cards:
            if i.__eq__(c):
                flag=1
                break
        if flag ==1:
            return True
        else:
            return False
        
        pass
    
    
    def shuffle(self):
        return random.shuffle(self.cards)
    
        pass
    
    
    def assert_full(self):
        lst=[]
        for i in self.cards:
            if i in lst:
                assert i in lst==True, "Repetition in the Deck"
            else:
                lst.append(i)
        assert len(self.cards)==52, "There should be 52 cards in a deck"
        pass
    
    # takes card from from deck, appends it to end, and returns it
    def draw(self):
        c=self.cards[0]
        self.cards.pop(0)
        self.cards.append(c)
        return c
        pass
    
    # sorts high to low
    def sort(self):
        return self.cards.sort(reverse=True)
        
    pass

# builds and returns complete deck except for cards in hands
def build_remaining_deck(hands):
    answer_deck=Deck()
    for i in range(0,52):
        answer_deck.add_card(card_from_num(i))
    
    for h in hands:
        for c in h.cards:
            if answer_deck.contains(c):
                answer_deck.cards.remove(c)
    return answer_deck
        
