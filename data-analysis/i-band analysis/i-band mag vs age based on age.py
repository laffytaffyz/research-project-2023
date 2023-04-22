import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
import math

# processing data and removing outliers
df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\i-band red clump.csv", encoding='latin-1')
df = df.drop(df[df['m_i']-df['m-M']-1.5424*df['reddening'] > 4].index)
mag = df['m_i']-df['m-M']-1.5424*df['reddening']
age = np.log10(np.array((10**6)*df['age']))

# calculating properties of young red clump
youngdf = df[df['age'] < 2000]
youngmag = np.array(youngdf['m_i']-youngdf['m-M']-1.5424*youngdf['reddening'])
youngage = np.log10(np.array((10**6)*youngdf['age']))

# calculating properties of old red clump
olddf = df[df['age'] > 2000]
oldmag = np.array(olddf['m_i']-olddf['m-M']-1.5424*olddf['reddening'])
oldage = np.log10(np.array((10**6)*olddf['age']))

# defining y and x values for statistical OLS analysis
youngx = youngage
oldx = oldage
youngy = youngmag
oldy = oldmag
younganalysis = smf.ols(formula = 'youngmag ~ youngage', data = youngdf).fit() 
oldanalysis = smf.ols(formula = 'oldmag ~ oldage', data = olddf).fit() 
analysis = smf.ols(formula = 'mag ~ age', data = df).fit()
print("YOUNG", younganalysis.summary())
print("OLD", oldanalysis.summary())
print("ALL", analysis.summary())

# creating plot with regression and labels
fig, ax = plt.subplots()
ax.invert_yaxis()
ax.set_title(r'$M_I$' + ' vs. Age Plot Separated by Age')
ax.set_ylabel(r'$M_I$ (mag)') 
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

# vertical line to separate old and young red clump
ax.axvline(math.log10(2000*(10**6)), color = "black", linestyle = "--", linewidth = 1.0)

plt.show()
