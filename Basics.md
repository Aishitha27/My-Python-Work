# If , Else, ElseIf Statements


```python
age = int(input("please enter your age : "))
if age >= 21:
    print("you can enter the bar area")
elif age < 21 and age > 18:
    print("you can enter the bar area, but cannot have alcohol")
else:
    print("i'm sorry you cannot enter")
```

    please enter your age : 17
    i'm sorry you cannot enter
    


```python
age = int(input("please enter your age : "))
if age >= 21:
    print("you can enter the bar area")
elif age < 21 and age > 18:
    print("you can enter the bar area, but cannot have alcohol")
else:
    print("i'm sorry you cannot enter")
```

    please enter your age : 20
    you can enter the bar area, but cannot have alcohol
    


```python
age = int(input("please enter your age : "))
if age >= 21:
    print("you can enter the bar area")
elif age < 21 and age > 18:
    print("you can enter the bar area, but cannot have alcohol")
else:
    print("i'm sorry you cannot enter")
```

    please enter your age : 25
    you can enter the bar area
    

# Def add


```python
def Mult(a, b):
    c = a * b
    if c == 0:
        return 0
    else:
        return c

result = Mult(12, 2)
print(result)
```

    24
    

# Def square


```python
def square(a):
    c = a*a 
    if c == 0:
        return 0
    else:
        return c

result = square(2)
print(result)
```

    4
    

# If , Else Statement


```python
def type_of_album(artist, album, year_released):
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)
```

    Oldie
    

# Def condition


```python
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks, it's rating is",rating)
    else:
        print("this album is good, it's rating is",rating)

isGoodRating(10)
```

    this album is good, it's rating is 10
    


```python
myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
    
print("Deep Purple rating is", getBandRating("Deep Purple"))
print("AC/DC rating is", getBandRating("AC/DC"))
```

    Deep Purple rating is 0.0
    AC/DC rating is 10.0
    

# Pandas


```python
import pandas as pd
x = {'Student':['David','Samuel','Terry','Evan'],
     'Age':['27', '24' , '22' , '32'],
     'Country' : ['UK','Cananda', 'China', 'USA'], 
     'Course' : ['Python', 'Data Structures', 'Machine Learning',
                 'Web Development'], 'Marks': ['85', '72', '89', '76']}
df=pd.DataFrame(x)
print(df.head())
```

      Student Age  Country            Course Marks
    0   David  27       UK            Python    85
    1  Samuel  24  Cananda   Data Structures    72
    2   Terry  22    China  Machine Learning    89
    3    Evan  32      USA   Web Development    76
    


```python
print(df.iloc[0,3])
```

    Python
    


```python
print(df.loc[2,'Country'])
```

    China
    
