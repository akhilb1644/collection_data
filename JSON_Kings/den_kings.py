import json

"""
The purpose of this program is to print the number of Danish monarchs that are a part of each dynasty(I'm too lazy to count) from the time mentioned below. As a lazy
programmer, I decided that making a program was the way to go. So, here we are.
"""

kings = open('den_kings.json') # File only contains Danish rulers from around the year 936 to 1448(doesn't include legendary or semi-legendary kings like Cnut I)

data = json.load(kings)
dynasties = list(data.values())
dynasties = sorted(dynasties)
dyns = list(set(dynasties))
king_dyns = dict()

count = 0
for dynasty in dyns:
    dynasties_2 = [d for d in dynasties if d != dynasty]
    count = len(dynasties) - len(dynasties_2)
    king_dyns[dynasty] = count

print(king_dyns) # Result is in 'result.txt' in the 'JSON_Kings' folder
