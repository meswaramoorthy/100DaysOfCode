import json
from difflib import get_close_matches

data = {}


def loaddata(fileName):
    """Loads the json file and returns a dictionary"""
    return json.load(open(fileName, "r"))


def findword(word):
    """Finds the word in the dicitonay and returns the definations as a list"""
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return  data[word.upper()]
    else:
        closematch = get_close_matches(word, data.keys())
        if len(closematch) > 0:
            reconfirm = input("Did you mean %s instead? Y or N " %closematch[0])
            if reconfirm.upper() == 'Y':
                return data[closematch[0]]
            else:
                return  "Word not found in the dictionary."
        else:
            return "Word not found in the dictionary."


data = loaddata("data.json")

word = input("Enter the word: ").lower()

outputlist = findword(word)

if type(outputlist) is list :
    for item in outputlist:
        print("{0}. {1}".format(outputlist.index(item) + 1, item))
else:
    print(outputlist)


