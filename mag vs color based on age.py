import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\red clump.csv")
df = df.dropna()
df = df.drop(df[df['J-K']>0.8].index)

mag = np.array(df['MK'])
color = np.array(df['J-K'])

youngdf = df[df['Age'] < 2000]
youngmag = np.array(youngdf['MK'])
youngcolor = np.array(youngdf['J-K'])

olddf = df[df['Age'] > 2000]
oldmag = np.array(olddf['MK'])
oldcolor = np.array(olddf['J-K'])

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

youngline = np.linspace(youngx.min(), youngx.max(), 100) 
youngmodel = np.poly1d(np.polyfit(youngx, youngy, 1)) 
ax.plot(youngline, youngmodel(youngline), c='blue',linewidth=1.0)

oldline = np.linspace(oldx.min(), oldx.max(), 100) 
oldmodel = np.poly1d(np.polyfit(oldx, oldy, 1)) 
ax.plot(oldline, oldmodel(oldline), c='red',linewidth=1.0)

line = np.linspace(color.min(), color.max(), 100) 
model = np.poly1d(np.polyfit(color, mag, 1)) 
ax.plot(line, model(line), c='black',linewidth=1.5)

# ax.text(0.68, -1.85, r"$M_{K,young} = (-0.8684 \pm 0.981)*(J-K)_0 + (-1.0940 \pm 0.590)$", fontsize = 8)
# ax.text(0.7, -1.81, r"$M_{K,old} = (-1.2298 \pm 1.868)*(J-K)_0 + (-0.7757 \pm 1.121)$",  fontsize = 8)
# regular mk is (-1.2452 +- 0.812)*color + (-0.8338 +- 0.491)

plt.show()