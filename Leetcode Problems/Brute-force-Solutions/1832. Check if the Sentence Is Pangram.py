sentence = "thequickbrownfoxjumpsoverthelazydog"
def pangram(sentence):
    d1 = {}
    for i in sentence:
        if i.isalpha():
            d1[i] = d1.get(i, 0) + 1
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    d2 = {}
    for i in alphabets:
        d2[i] = d2.get(i, 0) + 1
    for i in d2:
        if d1.get(i, 0) - d2[i] < 0:
            return False
    return True
print(pangram(sentence))