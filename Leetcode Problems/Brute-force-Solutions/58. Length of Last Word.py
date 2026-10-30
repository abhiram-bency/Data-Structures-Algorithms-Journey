s = "Hello world!"
def length_of_last_word(s):
    l = s.split()
    return len(l[-1])
print(length_of_last_word(s))