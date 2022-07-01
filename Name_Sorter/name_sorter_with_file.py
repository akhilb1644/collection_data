"""Reading a file and determining most common names present in it"""

with open('names.txt') as names:
    names = names.read()

names = names.split(",") # Changes the string into a list and separating based on where commas are

name_occurence = dict() # Making an empty dictionary for storing name and occurence

for name in names: # Counts the occurences of each name
    try:
        name_occurence[name] += 1
    except KeyError:
        name_occurence[name] = 1

name_occ_list = sorted(name_occurence.items(),key=lambda x: x[1],reverse=True) # Sorting names from most common to least

for name in name_occ_list: # Going through list
    space = 20 - len(name[0])
    spaces = " " * space # This line an previous one are just for formatting purposes
    print(f"name:{name[0]}{spaces}occurence: {name[1]}")
