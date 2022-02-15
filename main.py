import pandas as pandas
import numpy as np
import matplotlib.pyplot as plt

# TODO fix graph axis

vix = pandas.read_csv('vix-daily.csv')
print('VIX (fear index):\n\tmax single-day value:', vix.Close.max())
print('\tmin single-day value:', vix.Close.min())

vti = pandas.read_csv('vti.csv')
print('\nVTI:\n\tmax single-day value:', vti.Close.max())
print('\tmin single-day value:', vti.Close.min())

# vti['Close'].plot()
# plt.show()

fskax = pandas.read_csv('fskax.csv')
print('\nFSKAX:\n\tmax single-day value:', fskax.Close.max())
print('\tmin single-day value:', fskax.Close.min())

vtsax = pandas.read_csv('vtsax.csv')
print('\nVTSAX:\n\tmax single-day value:', vtsax.Close.max())
print('\tmin single-day value:', vtsax.Close.min())

vix['Date'] = pandas.to_datetime(vix['Date'], format = '%Y-%m-%d')
vix.set_index(['Date'], inplace=True)
vix['Close'].plot()

# vti['Date'] = pandas.to_datetime(vti['Date'], format = '%d/%m/%y')
# vti.set_index(['Date'], inplace=True)
# vti['Close'].plot()

plt.title('Volatility Index (VIX)')
plt.xlabel('Date')
plt.ylabel('Index')
plt.show()

# data visualizations: https://www.analyticsvidhya.com/blog/2021/07/stock-prices-analysis-with-python/
# Check out dataframe.corr() method for correlations
