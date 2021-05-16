from typing import List
import math
from linear_algebra import dot
from pydataset import data
from matplotlib import pyplot as plt

user = [30,50,40,23,18,14,10,78,99,102,105]
number_of_friends= [100,400,50,100,150,200,230,78,45,12,101]
number_of_minutes = [2,4,5,10,14,24,33,45,17,72,2504]


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

def de_mean(xs: List[float]) -> List[float]:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    assert len(xs) >= 2, "Varianca kerkon te pakten 2 elemente"
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)
def sum_of_squares(v) -> float:
    return dot(v, v)
def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))


def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "x dhe y duhen te kene numrin e njejte te elementeve"
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

def correlation(xs: List[float], ys: List[float]) -> float:
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0

def quantile(xs , p):
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

def find_outliers(xs):
    low_quantile = quantile(xs,0.10)
    high_quantile = quantile(xs,0.90)
    removed_items = []
    for i in xs:
        if (i < low_quantile or i > high_quantile):

            removed_items.append(xs.index(i))
    return removed_items


if (len(find_outliers(number_of_friends))>0):
        print ('Sygjerohen te hiqen përdoruesit me id: ')
        for i in find_outliers(number_of_friends):
            print (user[i])
elif (len(find_outliers(number_of_minutes))>0):
    print ('Sygjerohen te hiqen përdoruesit me id: ')
    for i in find_outliers(number_of_minutes):
        print (user[i])
print (correlation(user, number_of_friends))
print (correlation(user, number_of_minutes))
print (correlation(number_of_friends, number_of_minutes))
if correlation(user, number_of_friends)>0.9:
    print ('Korrelacion i madh mes perdoruesve dhe numrit te shokeve')
if correlation(user, number_of_minutes)>0.9:
    print ('Korrelacion i madh mes perdoruesve dhe numrit te minutave')
if correlation(number_of_friends, number_of_minutes)>0.9:
    print ('Korrelacion i madh mes shokeve dhe numrit te minutave')
plt.scatter(number_of_friends, number_of_minutes) #vizualizo

for user, number_of_friends, number_of_minutes in zip(user, number_of_friends, number_of_minutes):
    plt.annotate(user, xy=(number_of_friends, number_of_minutes),xytext=(5, -5),textcoords='offset points') #vendos ne scatter edhe shtetet

plt.title("Korelacioni ne mes numrit te shokeve me minutat e kaluara")
plt.xlabel("Numri i shokeve")
plt.ylabel("Koha e kaluar")
plt.show()

