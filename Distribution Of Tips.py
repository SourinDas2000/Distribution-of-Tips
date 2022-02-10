
import matplotlib.pyplot as plt

import pandas as pd


plt.style.use('seaborn')


# Reading Data :
    
data = pd.read_csv('Tips Data.csv')

tip = data['tip']


# Plotting histogram :
    
bins = [1, 2, 4, 6, 8, 10]

plt.hist(tip, bins = bins, edgecolor = 'black', label = 'Tips', alpha = 0.65)


# Average tip :
    
mean_tip = tip.mean()

color = 'Red'

plt.axvline(mean_tip, color = color, label = 'Average') 


# Labeling :
    
plt.legend()

plt.title('Distribution Of Tips In Dollars')

plt.xlabel('Tips Amount $ >>>', fontsize = 14)
plt.ylabel('Frequency >>>', fontsize = 14)

plt.tight_layout()

plt.show()


''' Created By Sourin Das '''
