def find(a, b):
        result = []
        for i in range(len(a)):
            if(a[i] != b[i]):
                result.append(i)
        return result

def swap(array, index1, index2):
        array[index1], array[index2] = array[index2], array[index1]


def areSimilar(a, b):
    pair = find(a, b)
    if len(pair) == 0:
        return True
    if len(pair) == 2:
        swap(a, pair[0], pair[1])
        pair = find(a, b)
        return len(pair) == 0
    return False

    
