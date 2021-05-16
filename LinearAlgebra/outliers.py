
vargu1 = [-500, 5,6,7,8,45,4,7,5,2, 200]

def median_odd(xs):
    return sorted(xs)[len(xs) // 2]
def median_even(xs):
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2
def median(v):
    return median_even(v) if len(v) % 2 == 0 else median_odd(v)
def mean(v):
    return sum(v)/len(v)
def distributions(xs):
    if (median(xs) == mean(xs)):
        return 'Distribuim normal'
    elif (median(xs) > mean(xs)):
        return 'Distribuim me anim djathtas'
    else:
        return'Distribuim me anim majtas'

def quantile(xs , p):
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

def remove_outliers(xs):
    low_quantile = quantile(xs,0.10)
    high_quantile = quantile(xs,0.90)
    perjashtimet = "Perjashtimet: "
    for i in xs:
        if (i < low_quantile or i > high_quantile):
            xs.remove(i)
            perjashtimet +=str(i)+ " "
    print (perjashtimet)
    return xs
print (quantile(vargu1, 0.10))
print (quantile(vargu1, 0.90))
print ("Vargu i rregulluar: " + str(remove_outliers(vargu1)))
