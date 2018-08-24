import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('E:\Coding\Python\Country Growth Visualization\countries.csv')

us = data[data.country == 'United States']
china = data[data.country == 'China']
india = data[data.country == 'India']

plt.title('Relative Population Growth')
plt.xlabel('Year')
plt.ylabel('Population Relative to 1953')
plt.plot(us.year, us.population / us.population.iloc[0])
plt.plot(china.year, china.population / china.population.iloc[0])
plt.plot(india.year, india.population / india.population.iloc[0])
plt.legend(['United States', 'China', 'India'])
plt.show()
