#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:09:09 2020

@author: pranavmanjunath
"""

# import statements here
from card import Card, card_from_num
from deck import Deck, build_remaining_deck
from future import FutureCards

def hand_from_string(s, fc):
    s=s.split()
    hand=Deck()
    for i in s:
        if i[0]=='?' and i[1:].isdigit():
            c=hand.add_empty_card()
            fc.add_future_card(int(i[1:]),c)
        else:
            hand.add_card(Card(i[0],i[1]))
    #print(hand)
    #print(fc)
    return hand
    pass

def read_input(file, fc):
    all_hands=[]
    with open(file) as f:
        for line in f:
            hand=hand_from_string(line,fc)
            all_hands.append(hand)

    return all_hands
    #return list of hands
    pass

#read_input('test.txt',fc=FutureCards())