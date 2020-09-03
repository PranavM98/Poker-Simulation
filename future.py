#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:08:32 2020

@author: pranavmanjunath
"""

from deck import Deck
from card import Card, card_from_num
class FutureCards:
    '''Class for futurecards'''
    
    def __init__(self):
        self.future_cards=[]
    
    def __str__(self):
        string=''
        for i in range(len(self.future_cards)):
            for j in range(len(self.future_cards[i].cards)):
                c=self.future_cards[i].cards[j]
                if j==len(self.future_cards[i].cards)-1:
                    string=string+c.__str__()
                else:
                    string = string+c.__str__()+ " "
            if i !=len(self.future_cards)-1:
                string=string+'\n'
        
        
        return(string)
        pass
    
    
    def __repr__(self):
        string='FutureCards:\n'
        for i in range(len(self.future_cards)):
            head='?'+str(i)+': '
            body=''
            for j in range(len(self.future_cards[i].cards)):
                c=self.future_cards[i].cards[j]
                if j==len(self.future_cards[i].cards)-1:
                    body=body+c.__str__()
                else:
                    body = body+c.__str__()+ " "
                
            row=head+body
            if i == len(self.future_cards)-1:
                string=string+row
            else:
                string=string+row+'\n'
        return(string)
        pass
    
    def add_future_card(self,index,card):

        if index >= len(self.future_cards):
       	

            for i in range((len(self.future_cards)),index+1):        
                self.future_cards.append(Deck())

        
            self.future_cards[index].add_card(card)
           
        else:
            self.future_cards[index].add_card(card)
            

            
    def future_cards_from_deck(self,d):
        for i in range(len(self.future_cards)):
            c=d.draw()
            for j in range(len(self.future_cards[i].cards)):
                self.future_cards[i].cards[j].value=c.value
                self.future_cards[i].cards[j].suit=c.suit
                
                    
            
        #Iterate over deck from range 0 to len(future_cards)
        #c=d.draw()
        #For i in range 0 to len(Future_Cards)
        # for j in range 0 to len(future_cards[i])
        #replace all cards with c
        pass