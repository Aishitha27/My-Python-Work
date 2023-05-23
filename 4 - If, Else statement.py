# -*- coding: utf-8 -*-
"""
Created on Tue May 23 20:42:30 2023

@author: Cashapona
"""

def type_of_album(artist, album, year_released):
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)


