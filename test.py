import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

a1 = -0.2424
a0 = -1.6421
dependent_variable = 'FeH'
regressiontype = 0

df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\red clump.csv")
df = df.dropna()

olddf = df[df['Age'] < 2000]
youngdf = df[df['Age'] > 2000]

# estimateddf = a1*np.log10(df[dependent_variable]*(10**6)) + a0
# estimateddf = a1*df[dependent_variable] + a0
# residualsdf = df['MK'] - estimateddf
# residualsstd = np.array(residualsdf).std()
# print(residualsstd)

fig, (regularplot, youngplot, oldplot) = plt.subplots(1,3)
xmax = oldplot
regularplot.scatter(x1,y1, color='green', s = 10)
regularplot.set(xlim=(, 100), ylim=(0, 100))

youngplot.scatter(x2,y2, color='red', s = 10)
youngplot.set(xlim=(0, 100), ylim=(0, 100))

oldplot.scatter(x3,y3, color='blue', s = 10)
oldplot.set(xlim=(0, 100), ylim=(0, 100))

# fig, ax = plt.subplots()
# plt.title(r'Estimated $M_K$ from Metallicity vs Actual $M_K$ of All RC Stars')
# plt.xlabel(r'$M_{K, actual}$ (mag)')
# plt.ylabel(r'$M_{K, estimated}$ (mag)') 
# ax.scatter(df['MK'], estimateddf)

# lims = [np.min([ax.get_xlim(), ax.get_ylim()]), np.max([ax.get_xlim(), ax.get_ylim()])]
# ax.set_aspect('equal')
# ax.set_xlim(lims)
# ax.set_ylim(lims)

# plt.plot(lims, lims, '-k', zorder=0, lw=1)
# plt.plot(lims, lims + residualsstd, '--k', zorder=0, lw=1) 
# plt.plot(lims, lims - residualsstd, '--k', zorder=0, lw=1) 

plt.show()