import json
from difflib import get_close_matches

# open json in data vareable
data = json.load(open("data.json"))

# function is cerated using translate method
def translate(w):
    # user input is upper case word it will change to lower
    w = w.lower()
    # condition added to check user give a proper word
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn =input("Did you mean %s insted? Enter Y if yes, or N if no:" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exits. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it."
            


# user to give input word 
word = input("Enter word: ")

print(translate(word))