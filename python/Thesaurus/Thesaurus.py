import json
from difflib import get_close_matches

data = json.load(open("data.json"))
print(type(data))
word = input("Enter the word : ").lower()


def meaning(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y if yes or N for no : " % get_close_matches(word, data.keys())[0])
        if yn.lower() == "y":
           return meaning(get_close_matches(word,data.keys())[0])
        else:
            return "We didn't understand your entry. Thanks for using Thesaurus"
    else:
        return "Word not found!"


output = meaning(word)

if type(output) == list:
    for text in output:
        print(text)
else:
    print(output)