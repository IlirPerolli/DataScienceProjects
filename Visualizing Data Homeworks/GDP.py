from matplotlib import pyplot as plt
years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019] #vendos vitet
kosovo_gdp = [3.31,4.375,2.81,3.44,1.222,4.095,4.071,4.226,3.816,4.172] #vendos gdp per secilin shtet
north_macedonia_gdp = [3.359,2.34,-0.456,2.925,3.629,3.856,2.848,1.082,2.9,3.2]
serbia_gdp = [0.731,2.036,-0.682,2.893,-1.59,1.806,3.339,2.101,4.495,4.249]
united_states_gdp = [2.564,1.551,2.25,1.842,2.526,2.908,1.638,2.37,2.927,2.161]
plt.plot(years,kosovo_gdp, color='red', marker='o', linestyle='solid') #vizualizo
plt.plot(years,north_macedonia_gdp, color='green', marker='o', linestyle='solid')
plt.plot(years,serbia_gdp, color='blue', marker='o', linestyle='solid')
plt.plot(years,united_states_gdp, color='black', marker='o', linestyle='solid')


plt.text(2015,-1.4,"Kosova", color='red') #shkruaj tekstin
plt.text(2017,-1.4,"Maqedonia e Veriut", color='green')
plt.text(2015,-1.67,"Serbia", color='blue')
plt.text(2017,-1.67,"Amerika", color='black')

plt.title('Rritja e GDP (% vjetor) ') #shkruaj titullin
plt.ylabel('GDP')
plt.xlabel('Vitet')
plt.show()
