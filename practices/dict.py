from collections import Counter
from typing import List
import random
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
friendships = {i['id']:[] for i in users}
for i,j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
def how_many_friends(user):
    return len (friendships[user])
print (how_many_friends(1))

print (friendships)
sorted_array = sorted(friendship_pairs, key=lambda item: item[1], reverse=True)
print (sorted_array)
try:
    0/0
except:
    print ('Nuk mund te pjesetoni me 0')

print (friendships.get(0))

array = [i for i in range(5)]
print (array)

array1 = [1,2,3,4,5]
array2 = [4,5,6,7,8]
array3 = sum([i+j for i, j in zip(array1, array2)])
print (array3)
def total(xs: list) -> float:
    return sum(total)

random_nr = random.choice([i for i in range(11)])
# random_nr = random.random([i for i in range(11)])
print (random_nr)

vargu = [i for i in range(11)]

print (vargu)

coordinates = (3,4)
print (coordinates[0])

dicti = ['ilir','ilir','ilir','ibrahim']
dicti = set(dicti)
counteri = Counter(dicti)
# counteri = sorted(counteri, reverse=False)
print (counteri)

print (random.random())
print (random.choice([1,2,3,45,656]))
print (random.randint(1,5))
print (random.choice([i for i in range(6)]))