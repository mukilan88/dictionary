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
    # if the user input lower case in this elif part title will be converted 
    # print the output directly
    elif w.title() in data:
        return data[w.title()]
    # if the user input upper case in this elif part title will be converted 
    # print the output directly
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn =input("Did you mean %s insted? Enter Y if yes, or N if no:" % get_close_matches(w, data.keys())[0])
        if (yn == "Y") or (yn == "y"):
            return data[get_close_matches(w, data.keys())[0]]
        elif (yn == "N") or (yn == "n"):
            return "The word doesn't exits. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it."
            


# user to give input word 
word = input("Enter word: ")

# print(translate(word)) it is not user friendly o/p get inside a array bracet
# output with nice line by line readable
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
