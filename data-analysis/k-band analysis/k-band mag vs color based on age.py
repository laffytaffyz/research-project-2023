import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

# processing data
df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\red clump.csv")
df = df.dropna()
df = df.drop(df[df['J-K']>0.8].index)
mag = np.array(df['MK'])
color = np.array(df['J-K'])

# calculating properties of young red clump
youngdf = df[df['Age'] < 2000]
youngmag = np.array(youngdf['MK'])
youngcolor = np.array(youngdf['J-K'])

# calculating properties of old red clump
olddf = df[df['Age'] > 2000]
oldmag = np.array(olddf['MK'])
oldcolor = np.array(olddf['J-K'])

# defining y and x values for statistical OLS analysis   
youngx = youngcolor
oldx = oldcolor
youngy = youngmag
oldy = oldmag
younganalysis = smf.ols(formula = 'MK ~ youngcolor', data = youngdf).fit() 
oldanalysis = smf.ols(formula = 'MK ~ oldcolor', data = olddf).fit() 
analysis = smf.ols(formula = 'MK ~ color', data = df).fit()
print("YOUNG", younganalysis.summary())
print("OLD", oldanalysis.summary())
print("ALL", analysis.summary())

# creating plot with regression and labels
fig, ax = plt.subplots()
ax.invert_yaxis()
ax.set_title(r'$M_K$' + ' vs.' + r'$(J-K)_0$' + ' Plot Separated by Age')
ax.set_ylabel(r'$M_K$ (mag)') 
ax.set_xlabel(r'$(J-K)_0$ (mag)') 
ax.scatter(youngx,youngy,s=10,c="blue") 
ax.scatter(oldx,oldy,s=10,c="red") 

# drawing fit lines
youngline = np.linspace(youngx.min(), youngx.max(), 100) 
youngmodel = np.poly1d(np.polyfit(youngx, youngy, 1)) 
ax.plot(youngline, youngmodel(youngline), c='blue',linewidth=1.0)

oldline = np.linspace(oldx.min(), oldx.max(), 100) 
oldmodel = np.poly1d(np.polyfit(oldx, oldy, 1)) 
ax.plot(oldline, oldmodel(oldline), c='red',linewidth=1.0)

line = np.linspace(color.min(), color.max(), 100) 
model = np.poly1d(np.polyfit(color, mag, 1)) 
ax.plot(line, model(line), c='black',linewidth=1.5)

plt.show()
