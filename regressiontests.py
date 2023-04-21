import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

# a1 = 9.275*(10**-6)
# a0 = -0.5625
# dependent_variable = 'age'
# regressiontype = 0

# a1 = -0.0942
# a0 = 0.166
# dependent_variable = 'age'
# regressiontype = 1

# a1 = -0.3989
# a0 = 3.4787
# dependent_variable = 'age'
# regressiontype = 2

# a1 = -0.7609
# a0 = 0.1301
# dependent_variable = 'color'
# regressiontype = 0

# a1 = -1.4821
# a0 = 0.6563
# dependent_variable = 'color'
# regressiontype = 1

# a1 = 0.0634
# a0 = -0.4982
# dependent_variable = 'color'
# regressiontype = 2

# a1 = 0.5916
# a0 = 0.4649
# dependent_variable = 'FeH'
# regressiontype = 0

a1 = 0.6496
a0 = 0.5056
dependent_variable = 'FeH'
regressiontype = 1

# a1 = 0.4174
# a0 = 0.2238
# dependent_variable = 'FeH'
# regressiontype = 2

df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\i-band red clump.csv", encoding='latin-1')
df = df.drop(df[df['m_i']-df['m-M']-1.5424*df['reddening'] > 4].index)

if (regressiontype == 1):
    df = df[df['age'] < 2000]
elif (regressiontype == 2):
    df = df[df['age'] > 2000]

if (dependent_variable == 'age'):
    estimateddf = a1*np.log10(df[dependent_variable]*(10**6)) + a0
elif (dependent_variable == 'FeH'):
    estimateddf = a1*df[dependent_variable] + a0
elif (dependent_variable == 'color'):
    estimateddf = a1*(df['m_v'] - df['m_i'] - 1.60*df['reddening']) + a0
mag = df['m_i']-df['m-M']-1.5424*df['reddening']
residualsdf = (mag) - estimateddf
rms = math.sqrt(((residualsdf**2).sum())/len(residualsdf))
print(rms)
residualsstd = np.array(residualsdf).std()

fig, ax = plt.subplots()
if (regressiontype == 0):
    rctype = r'All'
elif (regressiontype == 1):
    rctype = r'Young'
elif (regressiontype == 2):
    rctype = r'Old'
plt.title(r'Estimated $M_I$ from Metallicity vs Actual $M_I$ of ' + rctype + r' RC Stars')
plt.xlabel(r'$M_{I, actual}$ (mag)')
plt.ylabel(r'$M_{I, estimated}$ (mag)') 
ax.scatter(mag, estimateddf)
plt.axhline(mag.mean(),linestyle='--')
ax.text(-1.3, -0.6, r'Mean $M_I$',  fontsize = 12, c='#1f77b4')

lims = [np.min([ax.get_xlim(), ax.get_ylim()]), np.max([ax.get_xlim(), ax.get_ylim()])]
ax.set_aspect('equal')
ax.set_xlim(lims)
ax.set_ylim(lims)

plt.plot(lims, lims, '-k', zorder=0, lw=1)
plt.plot(lims, lims + residualsstd, '--k', zorder=0, lw=1) 
plt.plot(lims, lims - residualsstd, '--k', zorder=0, lw=1) 

plt.show()