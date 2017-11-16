import copy

def areSimilar(a, b):
    c = copy.copy(b)
    if a == c:
        return True
    list_len = len(a)
    for i in range(0, list_len):
        if a[i] in c:
            c.remove(a[i])
        else:
            return False
    if c == []:
        swapping = 0
        for j in range(0, list_len):
            if a[j] != b[j]:
                if a[j] in b:
                    b_index = b.index(a[j])
                    b[j], b[b_index] = b[b_index], b[j]
                    swapping += 1
        if swapping > 1:
            return False
        else:
            return True



