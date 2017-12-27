import json
data = json.load(open("data.json"))

def find(w):
    return data[w]

word = raw_input("Enter a word: ")

if word in data == True: #conditional to check whether the input is in the data set.
    print(find(word))
else:
    print("Uh-oh! This word isn't currently covered.")