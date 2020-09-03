#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:08:03 2020

@author: pranavmanjunath
"""

from card import Card, card_from_num
from deck import Deck

# finds flush suit
def find_flush(hand):
    d_suit={}
    for card in hand.cards:
        if card.suit in d_suit:
            d_suit[card.suit] += 1
        else:
            d_suit[card.suit] =1 
    #print(d_suit)
    for i,a in d_suit.items():
        if a>=5:
            return i

    return None   


        # makes dictionary of cards values to count of their occurances
def count_values(hand):
    d_value={}
    for card in hand.cards:
        if card.value in d_value:
            d_value[card.value] += 1
        else:
            d_value[card.value] =1
    d_value=dict(sorted(d_value.items(), key=lambda x: x[1], reverse=True))
    
    # #print(d_value)
    return d_value
    pass

# uses counts dict and returns a tuple (value with most n of a kind, n)
def get_max_count(hand, counts):
    lst=[]
    for k,v in counts.items():
        max_v=v
        break
        
    for k,v in counts.items():
        if max_v ==v:
            lst.append(k)

    
    max_k=max(lst)
    m=(max_k,max_v)
    
    return m
    pass

# finds index of second pair or returns -1 for no sec pair
def find_secondary_pair(hand, counts, val):
    sec_val=-1
    for k,v in counts.items():
        if k!=val:
            if v>=2:
                sec_val=k
    if sec_val==-1:
        return -1
    else:
        for i in range(len(hand.cards)):
            if hand.cards[i].value ==sec_val:
                return i
        

# get first index of value in hand
def get_kind_index(hand, value):
    for i in range(len(hand.cards)):
        if value==hand.cards[i].value:
            return i
    pass

# build hand with n of a kind starting at ind
def build_of_a_kind(hand, n, ind):
    d=Deck()
    for i in range(ind,ind+n):
        d.add_card(hand.cards[i])
    
    for i in range(len(hand.cards)):
        if hand.cards[i].value!=d.cards[0].value:
            d.add_card(hand.cards[i])
            if len(d.cards)==5:
                break
    return d    

    pass

# adds secondary pair (for full house or two pair)
def add_pair(hand,ind_s, ans_deck, ind_a):
    #print("INSIDE")
    #Full House
    if ind_a == 3:
        for i in range(ind_s,ind_s+2):
            for j in range(ind_a,ind_a+2):
                ans_deck.cards[j]=hand.cards[i]
                ind_a += 1
                break
    
    if ind_a ==2:
        for i in range(ind_s,ind_s+2):
            for j in range(ind_a,ind_a+2):
                ans_deck.cards[j]=hand.cards[i]
                ind_a += 1
                break
        
        for i in range(len(hand.cards)):

            if hand.cards[i].value != ans_deck.cards[0].value and hand.cards[i].value != ans_deck.cards[2].value:
                ans_deck.cards[len(ans_deck.cards)-1]=hand.cards[i]
                break
            
    #print(ans_deck)
    return ans_deck


    pass

# helper for is_straight_at
def is_n_length_straight_at(hand, ind, fs, n):
    pass

# helper for is_straight_at
def is_ace_low_straight_at(hand, ind, fs):
    pass

# if fs = None, look for any straight
# if fs = suit, look for straight in suit
# returns -1 for ace-low, 1 for straight, 0 for no straight
def is_straight_at(hand, ind, s):
    lst=[]
    if s is None:
        start=hand.cards[ind].value
        count=1
        for i in range(ind+1,len(hand.cards)):
            if hand.cards[i].value != start:
                if hand.cards[i].value == start-1:
                    count += 1
                    start=hand.cards[i].value

        #print(count)
        #straight    
        if count==5:
            return 1

        #ace low straight
        
        elif count==4:
            lst=[]
            for i in hand.cards:
                    lst.append(i.value)
         
            if 14 in lst and 2 in lst and 3 in lst and 4 in lst and 5 in lst:
                return -1
            else:
                return 0
        else:
            return 0
    else:
        start=hand.cards[ind].value
        start_s=hand.cards[ind].suit
        count=1
        for i in range(ind+1,len(hand.cards)):
            if hand.cards[i].value != start:
                if hand.cards[i].value == start-1 and hand.cards[i].suit == start_s:
                    count += 1
                    start=hand.cards[i].value
        #print("VALUE OF COUNT",str(count))
        if count ==5:
            return 1
        
        
        elif count == 4:
            lst=[]
            
            #ACE
            if hand.cards[0].suit==s:
                for i in hand.cards:
                    lst.append(i.value)
            
            
            if 14 in lst and 2 in lst and 3 in lst and 4 in lst and 5 in lst:
                return -1
            else:
                return 0
            
        else:
            return 0

        
    pass

# provided
def copy_straight(hand, ind, fs, ace_low=False):
    ans = Deck()
    last_card = None
    target_len = 5
    #print("INDEX",str(ind))
    #print("hand",hand)
    assert not fs or hand.cards[ind].suit == fs
    if ace_low:
        assert hand.cards[0].value == 14
        last_card = hand.cards[0]
        target_len = 4
        to_find = 5
        #ind += 1
        pass
    else:
        # regular straight
        to_find = hand.cards[ind].value
        pass
    while len(ans.cards) < target_len:
        #print(ind)
        if ind==len(hand.cards):
            break
        assert ind < len(hand.cards)
        if hand.cards[ind].value == to_find:
            if not fs or hand.cards[ind].suit == fs:
                ans.add_card(hand.cards[ind])
                to_find -= 1
                pass
            pass
        
        ind += 1

        pass
    #print(ans)
    if last_card is not None:
        ans.add_card(last_card)
        pass
    assert len(ans.cards) == 5
    #print("ANS")
    #print(ans)
    return ans

# provided
# looks for a straight (or straight flush if fs is not None)
# calls the student's is_straight_at for each index
# if found, copy_straight returns cards used for straight
def find_straight(hand, fs):
    for i in range(0, len(hand.cards) - 4):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == 1:
            # straight
            #print("INDEX:",str(i))
            return copy_straight(hand, i, fs)
        pass
    for i in range(0, len(hand.cards) - 3):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == -1:
            #print("-1")
            # ace-low straight
            return copy_straight(hand, i, fs, True)
        pass
    return None

# provided
# builds hand with flush suit fs
def build_flush(hand, fs):
    ans = Deck()
    i = 0
    while len(ans.cards) < 5:
        assert i < len(hand.cards)
        if hand.cards[i].suit == fs:
            ans.add_card(hand.cards[i])
            pass
        i += 1
        pass
    return ans

# provided
def evaluate_hand(hand):
    # straight flush
    fs = find_flush(hand)
    #print(fs)
    straight = find_straight(hand, fs)
    #print(straight)
    if fs and straight:
        return straight, 'straight flush'
    # four of a kind
    val_counts = count_values(hand)
    v, n = get_max_count(hand, val_counts)
    #print(v,n)
    assert n <= 4
    ind = get_kind_index(hand, v)
    #ind =5
    if n == 4:
        #print(n)
        return build_of_a_kind(hand, 4, ind), 'four of a kind'
    # full house
    sec_pair = find_secondary_pair(hand, val_counts, v)
    if n == 3 and sec_pair >= 0:
        ans = build_of_a_kind(hand, 3, ind)
        ans = add_pair(hand, sec_pair, ans, 3)
        return ans, 'full house'
    # flush
    if fs:
        return build_flush(hand, fs), 'flush'
    # straight
    if straight:
        return straight, 'straight'
    # three of a kind
    if n == 3:
        return build_of_a_kind(hand, 3, ind), 'three of a kind'
    # two pair
    if n == 2 and sec_pair >=0:
        ans = build_of_a_kind(hand, 2, ind)
        ans = add_pair(hand, sec_pair, ans, 2)
        return ans, 'two pair'
    # pair
    if n == 2:
        return build_of_a_kind(hand, 2, ind), 'pair'
    # high card
    ans = Deck()
    ans.cards = hand.cards[0:5]
    return ans, 'high card'

def num_from_rank(r):
    ranks = ['high card', 'pair', 'two pair', 'three of a kind', \
                 'straight', 'flush', 'full house', \
                 'four of a kind', 'straight flush']
    return ranks.index(r)

# returns positive if hand1 > hand2, 
# 0 for tie, or 
# negative for hand2 > hand1
    
    
def compare_hands(hand1,hand2):
    hand1.sort()
    hand2.sort()
    #print(hand1)
    #print(hand2)
    t1=evaluate_hand(hand1)
    t2=evaluate_hand(hand2)
    
    r1=num_from_rank(t1[1])
    r2=num_from_rank(t2[1])
    #print("RANK 1:",str(r1))
    #print("RANK 2:",str(r2))
    #print("ANS 1",t1[0])
    if r1>r2:
        #print("hand 1 is better")
        return +1
    elif r1<r2:
        #print("hand 2 is better")
        return -1
    else:
        #high card
        a1=t1[0]
        a2=t2[0]
        teq=0
        for i in range(len(a1.cards)):
            if a1.cards[i].value==a2.cards[i].value:
                teq += 1
            elif a1.cards[i].value>a2.cards[i].value:
                #print("A1")
                return 1
            else: 
                #print("A2")
                return -1
            
        if teq==5:
            #print("TIE")
            return 0
    


'''
   
d=Deck()
d.add_card(Card('0','s'))
d.add_card(Card('8','c'))
d.add_card(Card('7','c'))
d.add_card(Card('6','c'))
d.add_card(Card('5','c'))
d.add_card(Card('4','c'))
d.add_card(Card('2','c'))
d1=Deck()
d1.add_card(Card('J','s'))
d1.add_card(Card('0','c'))
d1.add_card(Card('8','s'))
d1.add_card(Card('7','c'))
d1.add_card(Card('6','s'))
d1.add_card(Card('5','h'))
d1.add_card(Card('4','d'))

ap=compare_hands(d,d1)
print(ap)
'''
