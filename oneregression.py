import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\i-band red clump.csv", encoding='latin-1')
kdf = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\red clump.csv", encoding='latin-1')
kdf = kdf.dropna()
df = df.drop(df[df['m_i']-df['m-M']-1.5424*df['reddening'] > 4].index)
mag = np.array(df['m_i']-df['m-M']-1.5424*df['reddening'])
color = np.array(df['m_v'] - df['m_i'] - 1.60*df['reddening'])
age = np.log10(np.array(df['age']))
feh = np.array(df['FeH'])
print(mag.mean())
print(mag.std())

exit()
print(age)
print(np.log10(np.array(kdf['Age'])))
print(feh)
print(np.array(kdf['FeH']))
x = np.append(age,np.log10(np.array(kdf['Age'])))
y = np.append(feh,np.array(kdf['FeH']))
# analysis = smf.ols(formula = 'y ~ x', data = df).fit() 
# print(analysis.summary())

# creating plot with regression and labels
# plt.title('Age vs. Metallicity Plot')
# plt.xlabel(r'$\log(Age)$ (dex)')
# plt.gca().invert_yaxis()
# plt.ylabel(r'$[Fe/H]$ (dex)') 
plt.scatter(x,y) 

line = np.linspace(x.min(), x.max(), 100) 
model = np.poly1d(np.polyfit(x, y, 1)) 
plt.plot(line, model(line), c='black',linewidth=1.0)

plt.show()