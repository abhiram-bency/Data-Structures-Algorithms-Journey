ransomnote = "aa"
magazine = "ab"

def function(ransomnote, magazine):
    d1 = {}
    for i in ransomnote:
        d1[i] = d1.get(i, 0) + 1
    d2 = {}
    for i in magazine:
        d2[i] = d2.get(i, 0) + 1
    
    for i in d1:
        if d2.get(i, 0) < d1[i]:
            return False
    return True
print(function(ransomnote, magazine))
