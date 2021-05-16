import math
def add(vec1, vec2):
   return [i+j for i,j in zip(vec1, vec2)]

def scalar(c,v):
    return [c*i for i in v]
print (scalar(2, [1, 2, 3]))

def dot(v1,v2):
    return sum([i*j for i,j in zip (v1,v2)])
def sum_of_squares(v1):
    return dot(v1,v1)
def median_odd(v1):
    v1 = sorted(v1)
    return v1[len(v1)//2]
def median_even(v1):
    v1 = sorted(v1)
    hi = len(v1)//2
    low = hi-1
    return (v1[hi]+v1[low])/2
def median(v1):
    return median_even(v1) if len(v1)%2 == 0 else median_odd(v1)

def quantile(v1,p):
    p_index = len(v1)*p
    return sorted(v1)[p_index]

def mean(v1):
    return sum(v1)/len(v1)

def de_mean(v1):
    x_bar = mean(v1)
    return [i - x_bar for i in v1]

def variance (v1):
    deviation = de_mean(v1)
    n = len(v1)
    return sum_of_squares(deviation)/(n-1)

def covariance(v1,v2):
    return dot(de_mean(v1),de_mean(v2))/(len(v1)-1)
def standard_deviation(v1):
    return math.sqrt(variance(v1))
def correlation(v1,v2):
    std1 = standard_deviation(v1)
    std2 = standard_deviation(v2)
    if std1 > 0 and std2 > 0:
        return covariance(v1,v2)/std1/std2
    else:
        return 0
print(dot([1, 2, 3], [4, 5, 6]))
print (sum_of_squares([1, 2, 3]))
print (median([1, 9, 2, 10]))