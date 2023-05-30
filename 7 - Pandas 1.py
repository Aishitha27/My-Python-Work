# -*- coding: utf-8 -*-
"""
Created on Tue May 23 20:42:30 2023

@author: Cashapona
"""

import pandas as pd
x = {'Student':['David','Samuel','Terry','Evan'],
     'Age':['27', '24' , '22' , '32'],
     'Country' : ['UK','Cananda', 'China', 'USA'], 
     'Course' : ['Python', 'Data Structures', 'Machine Learning',
                 'Web Development'], 'Marks': ['85', '72', '89', '76']}
df=pd.DataFrame(x)
print(df.head())

print(df.iloc[0,3])

print(df.loc[2,'Country'])





