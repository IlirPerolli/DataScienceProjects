from matplotlib import pyplot as plt
population = [ 1.873 , 2.077, 6.945, 2.862] #numri i popullates
gdp = [4.172, 3.2, 4.249, 2.24] #gdp e tyre
state = ['Kosovo', 'Maqedonia e veriut', 'Serbia', 'Albania'] #shtetet
plt.scatter(population, gdp) #vizualizo

for population, gdp, state in zip(population, gdp, state):
    plt.annotate(state, xy=(population, gdp),xytext=(5, -5),textcoords='offset points') #vendos ne scatter edhe shtetet

plt.title("Numri i banoreve vs. GDP")
plt.xlabel("Numri i banoreve (Milion)")
plt.ylabel("GDP")
plt.show()