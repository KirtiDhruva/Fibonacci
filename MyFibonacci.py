"""
Created on Fri Sep 18 12:21:14 2020

@author: dmwin
"""

from Fibonacci import Fibonacci
import matplotlib.pyplot as plt
import numpy as np

terms = 30

f = Fibonacci()

series_norm, _  =  f.get_series_normalised(terms)
ratios1, _  = f.get_ratios1(terms, 'reset')
ratios2, indexes = f.get_ratios2(terms, 'reset')

print(series_norm)
print(ratios1)
print(ratios2)

line1, = plt.plot(indexes, series_norm, marker='.', color='red', linestyle='', alpha=0.5)
line2, = plt.plot(indexes[:-1], ratios1, marker='<', color='blue', linestyle='', alpha=0.5)
line3, = plt.plot(indexes[:-1], ratios2, marker='>', color='green', linestyle='', alpha=0.5)

plt.xticks(range(indexes[0], indexes[-1]+1, 2), rotation=70)
plt.yticks(np.linspace(0, 2, 20), rotation=30)
plt.title('Fibonacci Stats')
plt.legend([line1, line2, line3], ['Normalised Series', 'Ratios1', 'Ratios2'])
plt.grid(linestyle='--')
plt.show()

stacked = np.vstack([ratios1, ratios2])

std = np.std(stacked, axis=1)
cov = np.cov(stacked)
corr = np.corrcoef(stacked)

print(f'Standard Deviation: \n{std}')
print(f'Covariance-Variance Matrix: \n{cov}')
print(f'Correlation Coefficient: \n{corr}')
