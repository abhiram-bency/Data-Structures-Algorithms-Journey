def rem_dup(arr):
    l = []
    for i in arr:
        if i in l:
            continue
        else:
            l.append(i)
    return l
arr = [2,2,2,2,2]
print(rem_dup(arr))