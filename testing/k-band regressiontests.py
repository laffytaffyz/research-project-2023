import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

# all of the regressions 
# regression types are as follows
# 0 - all red clump
# 1 - young red clump
# 2 - old red clump

a1 = -1.2452
a0 = -0.8338
dependent_variable = 'J-K'
regressiontype = 0

# a1 = -0.8684
# a0 = -1.0940 
# dependent_variable = 'J-K'
# regressiontype = 1

# a1 = -1.2298
# a0 = -0.7757
# dependent_variable = 'J-K'
# regressiontype = 2

# a1 = -0.2424
# a0 = -1.6421
# dependent_variable = 'FeH'
# regressiontype = 0

# a1 = 0.0992
# a0 = -1.5892
# dependent_variable = 'FeH'
# regressiontype = 1

# a1 = -0.2254
# a0 = -1.6033
# dependent_variable = 'FeH'
# regressiontype = 2

# a1 = 0.0043
# a0 = -1.6175
# dependent_variable = 'Age'
# regressiontype = 0

# a1 = -0.0382
# a0 = -1.3039
# dependent_variable = 'Age'
# regressiontype = 1

# a1 = 0.1893 
# a0 = -3.3526
# dependent_variable = 'Age'
# regressiontype = 2

# loading data
df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\red clump.csv")
df = df.dropna()

if (regressiontype == 1):
    df = df[df['Age'] < 2000]
elif (regressiontype == 2):
    df = df[df['Age'] > 2000]

# calculating estimated magnitudes
# estimateddf = a1*np.log10(df[dependent_variable]*(10**6)) + a0 # used for age which is log scale
estimateddf = a1*df[dependent_variable] + a0 # used for color and metallicity which are not log scale
residualsdf = df['MK'] - estimateddf
rms = math.sqrt(((residualsdf**2).sum())/len(residualsdf))
print(rms)  
residualsstd = np.array(residualsdf).std()

# makes estimated magnitude vs actual magnitude plots and calculating RMS
fig, ax = plt.subplots()
plt.title(r'Estimated $M_K$ from Metallicity vs Actual $M_K$ of Old RC Stars')
plt.xlabel(r'$M_{K, actual}$ (mag)')
plt.ylabel(r'$M_{K, estimated}$ (mag)') 
ax.scatter(df['MK'], estimateddf)
plt.axhline(df['MK'].mean(),linestyle='--')
ax.text(-1.68, -1.49, r'Mean $M_K$',  fontsize = 12, c='#1f77b4')

# sets y- and x-axis to be equal
lims = [np.min([ax.get_xlim(), ax.get_ylim()]), np.max([ax.get_xlim(), ax.get_ylim()])]
ax.set_aspect('equal')
ax.set_xlim(lims)
ax.set_ylim(lims)

# draws lines (identity line and those shifted by +/- 1 RMS)
plt.plot(lims, lims, '-k', zorder=0, lw=1)
plt.plot(lims, lims + residualsstd, '--k', zorder=0, lw=1) 
plt.plot(lims, lims - residualsstd, '--k', zorder=0, lw=1) 

plt.show()
