import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\i-band red clump.csv", encoding='latin-1')
df = df.drop(df[df['m_i']-df['m-M']-1.5424*df['reddening'] > 4].index)
mag = np.array(df['m_i']-df['m-M']-1.5424*df['reddening'])
color = np.array(df['m_v'] - df['m_i'] - 1.60*df['reddening'])

youngdf = df[df['age'] < 2000]
youngmag = np.array(youngdf['m_i']-youngdf['m-M']-1.5424*youngdf['reddening'])
youngcolor = np.array(youngdf['m_v'] - youngdf['m_i'] - 1.60*youngdf['reddening'])

olddf = df[df['age'] > 2000]
oldmag = np.array(olddf['m_i']-olddf['m-M']-1.5424*olddf['reddening'])
oldcolor = np.array(olddf['m_v'] - olddf['m_i'] - 1.60*olddf['reddening'])

youngx = youngcolor
oldx = oldcolor
youngy = youngmag
oldy = oldmag
younganalysis = smf.ols(formula = 'youngmag ~ youngcolor', data = youngdf).fit() 
oldanalysis = smf.ols(formula = 'oldmag ~ oldcolor', data = olddf).fit() 
analysis = smf.ols(formula = 'mag ~ color', data = df).fit()
print("YOUNG", younganalysis.summary())
print("OLD", oldanalysis.summary())
print("ALL", analysis.summary())

# creating plot with regression and labels
fig, ax = plt.subplots()
ax.invert_yaxis()
ax.set_title(r'$M_I$' + ' vs. ' + r'$(V-I)_0$' + ' Plot Separated by Age')
ax.set_ylabel(r'$M_I$ (mag)') 
ax.set_xlabel(r'$(V-I)_0$ (mag)') 
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

# ax.text(0.68, -1.85, r"$M_{K,young} = (0.1374 \pm 0.361)*(J-K)_0 + (-1.6926 \pm 0.0.233)$", fontsize = 8)
# ax.text(0.7, -1.81, r"$M_{K,old} = (-1.2298 \pm 1.868)*(J-K)_0 + (-0.7757 \pm 1.121)$",  fontsize = 8)
# regular mk is (-0.0249 +- 0.348)*color + (-1.5647 +- 0.219)
plt.show()