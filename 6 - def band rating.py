# -*- coding: utf-8 -*-
"""
Created on Tue May 23 20:42:30 2023

@author: Cashapona
"""

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
    
print("Deep Purple rating is", getBandRating("Deep Purple"))
print("AC/DC rating is", getBandRating("AC/DC"))



