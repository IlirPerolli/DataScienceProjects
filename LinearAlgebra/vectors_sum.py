v1 = [1,2,3,4]
v2 = [1,2,3,4]

def addVectors(v1, v2):
    return [i+j for i,j in zip(v1, v2)]

if (len(v1) == len(v2)):
    print (addVectors(v1,v2))
else:
    print('Vektoret kane gjatesi te ndryshme')