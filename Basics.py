#!/usr/bin/env python
# coding: utf-8

# # If , Else, ElseIf Statements

# In[7]:


age = int(input("please enter your age : "))
if age >= 21:
    print("you can enter the bar area")
elif age < 21 and age > 18:
    print("you can enter the bar area, but cannot have alcohol")
else:
    print("i'm sorry you cannot enter")


# In[8]:


age = int(input("please enter your age : "))
if age >= 21:
    print("you can enter the bar area")
elif age < 21 and age > 18:
    print("you can enter the bar area, but cannot have alcohol")
else:
    print("i'm sorry you cannot enter")


# In[9]:


age = int(input("please enter your age : "))
if age >= 21:
    print("you can enter the bar area")
elif age < 21 and age > 18:
    print("you can enter the bar area, but cannot have alcohol")
else:
    print("i'm sorry you cannot enter")


# # Def add

# In[10]:


def Mult(a, b):
    c = a * b
    if c == 0:
        return 0
    else:
        return c

result = Mult(12, 2)
print(result)


# # Def square

# In[13]:


def square(a):
    c = a*a 
    if c == 0:
        return 0
    else:
        return c

result = square(2)
print(result)


# # If , Else Statement

# In[14]:


def type_of_album(artist, album, year_released):
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)


# # Def condition

# In[15]:


def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks, it's rating is",rating)
    else:
        print("this album is good, it's rating is",rating)

isGoodRating(10)


# In[16]:


myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
    
print("Deep Purple rating is", getBandRating("Deep Purple"))
print("AC/DC rating is", getBandRating("AC/DC"))


# # Pandas

# In[20]:


import pandas as pd
x = {'Student':['David','Samuel','Terry','Evan'],
     'Age':['27', '24' , '22' , '32'],
     'Country' : ['UK','Cananda', 'China', 'USA'], 
     'Course' : ['Python', 'Data Structures', 'Machine Learning',
                 'Web Development'], 'Marks': ['85', '72', '89', '76']}
df=pd.DataFrame(x)
print(df.head())


# In[18]:


print(df.iloc[0,3])


# In[19]:


print(df.loc[2,'Country'])

