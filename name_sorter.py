""""This program will go through a list of names and list each name in order of occurence."""

names = ["Louis","Philip","Louis","Louis","Philip","Philip","John","Philip","Charles","Philip","John","Charles",
         "Charles","Henry","Charles","Louis","Charles","Louis","Francis","Henry","Francis","Henry","Henry","Louis",
         "Louis","Louis","Louis","Napoleon","Louis","Charles","Louis-Phillipe","Napoleon"] # List of names

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