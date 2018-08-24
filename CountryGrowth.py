import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('E:\Coding\Python\Country Growth Visualization\countries.csv')

us = data[data.country == 'United States']
china = data[data.country == 'China']
india = data[data.country == 'India']

countries = [us, china, india]

plt.title('Relative Population Growth')
plt.xlabel('Year')
plt.ylabel('Population Relative to 1953')
plt.legend(['United States', 'China', 'India'])

for country in countries:
    plt.plot(country.year, country.population / country.population.iloc[0])
    
plt.show()
