vargu1 = [1,2,3,4,5,6,7,8]
vargu2 = [2,4,6,8,200,12,14]
vargu3 = [-500,5,7,9,4,2,100,200]

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
def check_results(xs):
    print ("Mediana: "+ str(median(xs)))
    print ("Mesatarja: "+str(mean(xs)))
    print (distributions(xs))
    print ('')
check_results(vargu1)
check_results(vargu2)
check_results(vargu3)