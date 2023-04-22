import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

# data processing
df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\red clump.csv")
mag = np.array(df['MK'])
color = np.array(df['J-K'])
age = np.log10(np.array((10**6)*df['Age']))
feh = np.array(df['FeH'])

# defining y and x values for statistical OLS analysis 
x = age
y = feh
analysis = smf.ols(formula = 'y ~ x', data = df).fit() 
print(analysis.summary())

# creating plot with regression and labels
plt.title('Age vs. Metallicity Plot')
plt.xlabel(r'$\log(Age)$ (dex)')
# plt.gca().invert_yaxis()
plt.ylabel(r'$[Fe/H]$ (dex)') 
plt.scatter(x,y) 

# drawing fit lines
line = np.linspace(x.min(), x.max(), 100) 
model = np.poly1d(np.polyfit(x, y, 1)) 
plt.plot(line, model(line), c='black',linewidth=1.0)

plt.show()
