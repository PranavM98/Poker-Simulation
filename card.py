#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:06:38 2020

@author: pranavmanjunath
"""


def value_from_letter(letter):
    val_dictionary = {'A':14,'K':13,'Q':12,'J':11,'a':14,'k':13,'q':12,'j':11}
    if letter in val_dictionary:
        return val_dictionary[letter]


def check_suit(s):
    suit=['s','h','d','c','?']
    
    if isinstance(s,str):
    
        if s in suit:
            return s
        elif s is None:
            return '?'
        else:
            raise ValueError("Invalid Suit: {}".format(s))
    else:
        raise ValueError("Invalid Suit: {}".format(s))
        
def check_value(val):

    if val>=2 and val<=14:
        return True
    elif val==0:
        return True
    else:
        raise ValueError("Invalid Value: {}".format(val))


def letter_from_value(value):
    val_dictionary = {'A':14,'K':13,'Q':12,'J':11}
    if value ==0:
        return '?'
    if value<10:
        return str(value)
    elif value==10:
        return '0'
    else:
        for key,v in val_dictionary.items():
            if v==value:
                return key

def suit_ranking(s1,s2):
    s_rank=['c','d','h','s']
    if s_rank.index(s1)<s_rank.index(s2):
        return True
    else:
        return False


def list_card():
    lst=[]
    for i in ['2','3','4','5','6','7','8','9','0','J','Q','K','A']:
        for j in ['c','d','h','s']:
            lst.append(Card(i,j))
    return lst

def card_from_num(index):
    lst=list_card()
    return lst[index]



class Card:

    ''' A Class to represent a card with a value and suit'''

    def __init__(self,letter='?',suit='?'):
        if letter is '?' and suit is '?':
            self.value= 0
            self.suit = '?'

        elif letter is '?':
            raise ValueError("Invalid Value: {}".format(letter))
        elif suit is '?':
            raise ValueError("Invalid Suit: {}".format(suit))
        else:
            if letter is None:
                raise ValueError("Invalid Value: {}".format(letter))
            if isinstance(letter,int) or isinstance(letter,float):
                    raise ValueError("Invalid Value: {}".format(letter))
            elif letter.isdigit() and len(letter)==1:
                if int(letter)==0:
                    self.value=10
                elif check_value(int(letter)):
                    self.value=int(letter)

            elif letter in ['K','Q','J','A']:
                self.value=value_from_letter(letter)
            else:
                raise ValueError("Invalid Value: {}".format(letter))

            self.suit=check_suit(suit)
            
    def __str__(self):
        return('{}{}'.format(letter_from_value(self.value),self.suit))

    def __repr__(self):
        return('Card({}{})'.format(letter_from_value(self.value),self.suit))

    def __eq__(self,other):
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False

    def __lt__(self,other):
        if self.value==other.value:
            return suit_ranking(self.suit, other.suit)
        elif self.value<other.value:
            return True
        else:
            return False

    def is_valid(self):
        if check_value(self.value) and check_suit(self.suit):
            return True
        else:
            return False