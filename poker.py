#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:09:50 2020

@author: pranavmanjunath
"""

#!/usr/local/bin/python3

import sys
from future import FutureCards
from pinput import read_input
from deck import Deck,build_remaining_deck
from evaluate import compare_hands
from card import Card, card_from_num
from itertools import combinations

# provided
def print_results(wins, n):
    for i in range(0, len(wins) - 1):
        print('Hand {} won {} / {} times'.format(i, wins[i], n))
        pass
    print('and there were {} ties'.format(wins[len(wins) - 1]))
    pass



def game_combinations(all_hands,lst,a_list):

    for combo in combinations(all_hands,2):
            #print(combo)
            r=compare_hands(combo[0],combo[1])
            lst.append(r)
            #If hand 1 wins
            if r==1:
                a_list.append(combo[0])
            elif r==-1:
                a_list.append(combo[1])
            else:
                a_list.append('tie')
        
    return lst,a_list

def create_dictionary(d_val,a_list):
    for i in a_list:
            if i in d_val:
                d_val[i] +=1
            else:
                d_val[i] = 1
    d_val=dict(sorted(d_val.items(), key=lambda x: x[1], reverse=True))
    #print(d_val)

    #d_val is sorted with respect to value field (the hands with most wins would be first)

    for k,v in d_val.items():
        max_v=v
        max_k=k
        break
    return d_val,max_k,max_v
    
def main():
    # get count of command line arguments
    argc = len(sys.argv)
    #print(argc)
    
    #print(sys.argv[0])
    # check user input
    if argc==2:
        mc=10000
    elif argc>3:
        #print("TOO Many Arguments")
        exit()
    else:
        mc=int(sys.argv[2])

    file=str(sys.argv[1])
    

    #Call pipoker
    fc=FutureCards()
    all_hands=read_input(file,fc)
    #print("ALL HANDS",all_hands)
    r_deck=build_remaining_deck(all_hands)

    wins=[0]*(len(all_hands)+1)

    for i in range(0,mc):
        r_deck.shuffle()
        fc.future_cards_from_deck(r_deck)
        lst=[]
        
        for i in range(len( all_hands)):
            all_hands[i].sort()
        a_list=[]
        #Playing against all combinations and appending the result (0,1,-1) in lst
        #Appending the winning deck in a_list. If tie then 'tie' will be inputed in a_list

        lst,a_list=game_combinations(all_hands,lst,a_list)
        
            #print("NEW:",lst)
            #print("A_LIST",a_list)
        #d_val is a dictionary which contains the various winners (key)  and the number of times they won (value)
        d_val={}
        d_val,max_k, max_v=create_dictionary(d_val,a_list)
        #max_k will contain the most hand with the most wins and max_v will contain the times max_k won
        #lo  is a list that contains the hands with the maximum amount of wins
        lo=[]
        for k,v in d_val.items():
            if v==max_v:
                lo.append(k)

        # if the maximum number of wins was a tie or if there are multiple hands with the same number of wins, then increment the count of ties in the wins list
        
        if max_k=='tie' or len(lo)>1:
            wins[-1] += 1
        #len(lo) is 1 when only one hand has the most number of wins. Hence if the len(lo)=1, then identify which hand it is by comparing it with the all_hands deck and increment the value of the that index in wins list 
        elif len(lo)==1:
            for i in range(len(all_hands)):
                if lo[0] is all_hands[i]:
                #print("INDEX:",str(i))
                    wins[i] +=1 
            
    print_results(wins,mc)

    pass

if __name__ == '__main__':
    main()