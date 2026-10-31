words = ["leet", "code", "solution"]
x = "e"
def Find_Words_Containing_Character(words,x):
    l = []
    for index,i in enumerate(words):
        if x in i:
            l.append(index)
    return l
print(Find_Words_Containing_Character(words,x))
