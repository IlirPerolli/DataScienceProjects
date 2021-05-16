
xs = [1,4,8,10,22]
def mean(xs):
    return sum(xs)/len(xs)
def de_mean(xs):
    x_bar = int (mean(xs))
    return [x - x_bar for x in xs]
def datarange(xs):
    return max(xs) - min (xs)
def dot(xs,xs1):
    return sum(i*j for i,j in zip(xs, xs1))
def sum_of_squares(xs):
    return dot(xs,xs)
def variance(xs):
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n-1)
print (variance(xs))
def quantile(xs, p):
    position =int(p*len(xs))

    return sorted(xs)[position]

print (quantile(xs,0.9))

def covariance(xs, xs1):

    return dot(de_mean(xs), de_mean(xs1))/(len(xs)/1)
def standard_deviation(xs):
    return variance(xs)
def correlation(xs,ys):
    std1 = standard_deviation(xs)
    std2 = standard_deviation(ys)
    return covariance(xs,ys)/std1/std2
