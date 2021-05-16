def add(v1,v2):
    return [i+j for i, j in zip( v1,v2)]
print (add([1, 2, 3], [4, 5, 6]))

def dot(v1,v2):
    return sum([i*j for i,j in zip(v1,v2)])

def quantile(v1, p):
    p_index = int (len(v1)*p)
    return sorted(v1)[p_index]

vargu = [1,2,3,4,99,5]
print (quantile(vargu,0.1))