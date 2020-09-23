"""
Created on Fri Sep 18 12:21:14 2020
@author: Kirti Dhruva
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

plt.plot(indexes, series_norm, 'r.', alpha=0.5)
plt.plot(indexes[:-1], ratios1, 'b<', alpha=0.5)
plt.plot(indexes[:-1], ratios2, 'g>', alpha=0.5)

plt.xticks(range(indexes[0], indexes[-1]+1, 2), rotation=0)
plt.yticks(np.linspace(0, 2, 20), rotation=0)

plt.title('Fibonacci Stats')
plt.legend(['Normalised Series', 'Ratios1', 'Ratios2'])
plt.grid(color='gray', ls='-.', lw='0.25')

plt.gca().spines['right'].set_color('None')
plt.gca().spines['top'].set_color('None')
plt.show()

stacked = np.vstack([ratios1, ratios2])

std = np.std(stacked, axis=1)
cov = np.cov(stacked)
corr = np.corrcoef(stacked)

print(f'Standard Deviation: \n{std}')
print(f'Covariance-Variance Matrix: \n{cov}')
print(f'Correlation Coefficient: \n{corr}')
