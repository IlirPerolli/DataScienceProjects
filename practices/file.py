
file = open('file.txt', 'r').read().split()
for i in file:
    if (len(i)<5):continue
    print (i)
