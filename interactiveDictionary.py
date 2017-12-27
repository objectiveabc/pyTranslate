import json, difflib

data = json.load(open("data.json"))

def find(w):
    if w in data: #conditional to check whether the input is in the data set.
        return data[w]
    elif difflib.get_close_matches(w, data) != False:
        print ("Did you mean ", difflib.get_close_matches(w, data))
    else:
        return "Uh-oh! This word isn't currently covered."

word = raw_input("Enter a word: ")
print(find(word.upper())) #upper() - converts input and makes the query caps insensitive - assumes data.json is lower case