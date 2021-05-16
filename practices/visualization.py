from matplotlib import pyplot as plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
labels = ['adsf','adsf','adsf','adsf','adsf','adsf','adsf']
# plt.bar(years, gdp,color="red")
# plt.plot(years, gdp)
# plt.xticks([i for i in years])
plt.scatter(years,gdp)
for years, gdp, labels in zip(years, gdp, labels):
    plt.annotate(labels, xy=(years, gdp))
plt.show()