import json
from difflib import get_close_matches
data = json.load(open("076 data.json"))
def menu_driven():
    def meaning(w):
        w=w.lower()
        if w in data:
            return data[w]
        elif w.title() in data:
            return data[w.title()]
        elif w.upper() in data:
            return data[w.upper()]
        elif len(get_close_matches(w,data.keys()))>0:
            yn = input("Did you mean %s ? Type Y for yes, N for no: " %get_close_matches(w,data.keys())[0])
            if yn=='Y':
                return data[get_close_matches(w,data.keys())[0]]
            elif yn=='N':
                return "The word doesnot exist"
            else:
                return "Wrong input"
        else:
            return "The word doesnot exist"

    word = input("Enter word you want to search: ")
    output = meaning(word)
    if type(output)==list:
        for i in output:
            print (i)
    else:
        print (output)

while (True):
    menu_driven()
    t = input("Press 1 to search another word and 2 to exit ")
    if t=='2':
           break
