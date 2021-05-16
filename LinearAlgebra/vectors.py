from typing import List
Vector = List[float]
height_weight_age = [70, # inches,
                     170, # pounds,
                     40 ] # years
grades = [95, # exam1
          80, # exam2
          75, # exam3
          ] # exam4

def add(vector1 : Vector, vector2 : Vector )->Vector:

        return [v1+v2 for v1, v2 in zip(vector1, vector2)]

print (add(height_weight_age, grades))