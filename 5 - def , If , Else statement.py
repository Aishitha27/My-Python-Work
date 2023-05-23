# -*- coding: utf-8 -*-
"""
Created on Tue May 23 20:42:30 2023

@author: Cashapona
"""

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks, it's rating is",rating)
    else:
        print("this album is good, it's rating is",rating)

isGoodRating(10)



