# https://usaco.org/index.php?page=viewproblem2&cpid=1107
# 6:25 - 6:35
# 6:40 - 7:15

'''
bessie = 0
mildred = -
ox tiger rabbit dragon snake horse goat monkey rooster dog pig rat 

one list of names
one list of directions
one list of years
one list of related to whos

calculate years from bessie for each one

'''
from typing import NamedTuple

zodiac = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]
n = int(input().strip())

class Cow(NamedTuple):
    name: str
    previous: bool
    year: int
    who: str

cows = []
for i in range(n):
    c = input().strip().split()
    if c[3] == "previous":
        cows.append(Cow(c[0], True, zodiac.index(c[4]), c[7]))
    else:
        cows.append(Cow(c[0], False, zodiac.index(c[4]), c[7]))

years = {"Bessie": 0}

for c in cows:
    change = -1 if c.previous else 1
    this_year = years[c.who] + change
    while this_year % len(zodiac) != c.year:
        this_year += change
    years[c.name] = this_year
'''
for c in cows:
    if c.previous == True:
        relname, relyear = list(years.items())[len(years)-1]
        agefromrel = c.year - 12 + abs(relyear - c.year)
        years[c.name] = years[c.who] + agefromrel
    else:
        relname, relyear = list(years.items())[len(years)-1]
        agefromrel = 12 - c.year + abs(relyear - c.year)
        years[c.name] = years[c.who] + agefromrel
print(years)
'''

print(abs(years["Bessie"]-years["Elsie"]))
    

