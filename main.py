import json
from difflib import get_close_matches

#open Json File to capture data
data = json.load(open("data.json"))

#this is the translate function
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        print("I think you meant: " + word.capitalize())
        return data[word.capitalize()]
    elif word.upper() in data:
        print("I think you meant: " + word.upper())
        return data[word.upper()]
    else:
        #check for close words - put max tries at 3
        possibleWords = get_close_matches(word, data.keys(), 3)
        if (len(possibleWords) == 0):
            return "Word doesn't exist."
        for w in possibleWords:
            yesOrNo = input("Did you mean " + w + "?")
            if (yesOrNo.lower() == "y" or yesOrNo.lower() == "yes"):
                return data[w]
        return "Sorry, I can't find your word."

#print the definition returned by translate
def printDefinition(definition):
    if (type(definition) == list):
        for line in definition:
            print("\t-" + line)
    else:
        print(definition)


#Main code
print("Welcome to the Dictionary!")
userInput2 = "y"
#Reassert prompt if user wants to continue using the dictionary
while (userInput2.lower() == "y" or userInput2.lower() == "yes"):
    userInput = input("Please enter a word you'd like to look up: ")
    printDefinition(translate(userInput))
    userInput2 = input("Would you like to continue? ")
