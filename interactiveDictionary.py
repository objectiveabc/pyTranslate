import json
data = json.load(open("data.json"))

def find(w):
    if w in data: #conditional to check whether the input is in the data set.
        return data[w]
    else:
        return "Uh-oh! This word isn't currently covered."

word = raw_input("Enter a word: ")
print(find(word.lower())) #lower() - converts input and makes the query caps insensitive - assumes data.json is lower case