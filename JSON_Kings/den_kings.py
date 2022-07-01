import json

kings = open('den_kings_1.json')

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

print(king_dyns)