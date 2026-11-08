sentence = "thequickbrownfoxjumpsoverthelazydog"
def pangram(sentence):
    return len(set(sentence)) == 26
print(pangram(sentence))