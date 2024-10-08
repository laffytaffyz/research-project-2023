import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
import math

# processing data
df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\red clump.csv")
df = df.dropna()
mag = np.array(df['MK'])
age = np.log10(np.array((10**6)*df['Age']))

# calculating properties of young red clump
youngdf = df[df['Age'] < 2000]
youngmag = np.array(youngdf['MK'])
youngage = np.log10((10**6)*np.array(youngdf['Age']))

# calculating properties of old red clump
olddf = df[df['Age'] > 2000]
oldmag = np.array(olddf['MK'])
oldage = np.log10(np.array((10**6)*olddf['Age']))

# defining y and x values for statistical OLS analysis 
youngx = youngage
oldx = oldage
youngy = youngmag
oldy = oldmag
younganalysis = smf.ols(formula = 'MK ~ youngage', data = youngdf).fit() 
oldanalysis = smf.ols(formula = 'MK ~ oldage', data = olddf).fit() 
analysis = smf.ols(formula = 'MK ~ age', data = df).fit()
print("YOUNG", younganalysis.summary())
print("OLD", oldanalysis.summary())
print("ALL", analysis.summary())

# creating plot with regression and labels
fig, ax = plt.subplots()
ax.invert_yaxis()
ax.set_title(r'$M_K$' + ' vs. Age Plot Separated by Age')
ax.set_ylabel(r'$M_K$ (mag)') 
ax.set_xlabel('Log Age (dex)') 
ax.scatter(youngx,youngy,s=10,c="blue") 
ax.scatter(oldx,oldy,s=10,c="red") 

# drawing fit lines
youngline = np.linspace(youngx.min(), youngx.max(), 100) 
youngmodel = np.poly1d(np.polyfit(youngx, youngy, 1)) 
ax.plot(youngline, youngmodel(youngline), c='blue',linewidth=1.0)

oldline = np.linspace(oldx.min(), oldx.max(), 100) 
oldmodel = np.poly1d(np.polyfit(oldx, oldy, 1)) 
ax.plot(oldline, oldmodel(oldline), c='red',linewidth=1.0)

line = np.linspace(age.min(), age.max(), 100) 
model = np.poly1d(np.polyfit(age, mag, 1)) 
ax.plot(line, model(line), c='black',linewidth=1.5)

# vertical line to separate young and old red clump
ax.axvline(math.log10(2000*(10**6)), color = "black", linestyle = "--", linewidth = 1.0)

plt.show()
