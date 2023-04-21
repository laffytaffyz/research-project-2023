import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\i-band red clump.csv", encoding='latin-1')
df = df.drop(df[df['m_i']-df['m-M']-1.5424*df['reddening'] > 4].index)
mag = np.array(df['m_i']-df['m-M']-1.5424*df['reddening'])
feh = np.array(df['FeH'])

youngdf = df[df['age'] < 2000]
youngmag = np.array(youngdf['m_i']-youngdf['m-M']-1.5424*youngdf['reddening'])
youngfeh = np.array(youngdf['FeH'])

olddf = df[df['age'] > 2000]
oldmag = np.array(olddf['m_i']-olddf['m-M']-1.5424*olddf['reddening'])
oldfeh = np.array(olddf['FeH'])

youngx = youngfeh
oldx = oldfeh
youngy = youngmag
oldy = oldmag
younganalysis = smf.ols(formula = 'youngmag ~ youngfeh', data = youngdf).fit() 
oldanalysis = smf.ols(formula = 'oldmag ~ oldfeh', data = olddf).fit() 
analysis = smf.ols(formula = 'mag ~ feh', data = df).fit()
print("YOUNG", younganalysis.summary())
print("OLD", oldanalysis.summary())
print("ALL", analysis.summary())

# creating plot with regression and labels
fig, ax = plt.subplots()
ax.invert_yaxis()
ax.set_title(r'$M_I$' + ' vs. Metallicity Plot Separated by Age')
ax.set_ylabel(r'$M_I$ (mag)') 
ax.set_xlabel(r'$[Fe/H]$ (dex)') 
ax.scatter(youngx,youngy,s=10,c="blue") 
ax.scatter(oldx,oldy,s=10,c="red") 

youngline = np.linspace(youngx.min(), youngx.max(), 100) 
youngmodel = np.poly1d(np.polyfit(youngx, youngy, 1)) 
ax.plot(youngline, youngmodel(youngline), c='blue',linewidth=1.0)

oldline = np.linspace(oldx.min(), oldx.max(), 100) 
oldmodel = np.poly1d(np.polyfit(oldx, oldy, 1)) 
ax.plot(oldline, oldmodel(oldline), c='red',linewidth=1.0)

line = np.linspace(feh.min(), feh.max(), 100) 
model = np.poly1d(np.polyfit(feh, mag, 1)) 
ax.plot(line, model(line), c='black',linewidth=1.5)

# ax.text(-1.1, -1.85, r"$M_{K,young} = (0.0992 \pm 0.474)*[Fe/H] + (-1.5892 \pm 0.091)$", fontsize = 8)
# ax.text(-1.1, -1.81, r"$M_{K,old} = (-0.2254 \pm 0.150)*[Fe/H] + (-1.6033 \pm 0.075)$",  fontsize = 8)
# regular is mk = (-0.2424 +- 0.143)feh + (-1.6421 +- 0.049)

plt.show()