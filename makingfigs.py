# NGC6569 PARALLAX DISTRIBUTION
import matplotlib, matplotlib.pyplot as plt, pandas as pd, numpy as np
from scipy.stats import norm
import os

general_clusters_df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\Data (Other Versions)\\general cluster data.csv")
general_clusters_df.set_index("GES_FLD", inplace = True)
# plt.rc('font', **timesfont)

df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\NGC6569-result.csv")
general_cluster_df = general_clusters_df.loc["NGC6569"]
parallax = (df['parallax']/1000).sort_values()
n_bins = 100
plt.hist(parallax, bins=n_bins)
plt.title('Parallax Distribution of NGC 6569')
plt.xlabel('Parallax (arcseconds)')
plt.ylabel('N')

std = np.std(parallax)
mean = np.mean(parallax)
size = np.size(parallax)
plt.xlim([-0.00087, 0.0011])

plt.axvline(mean, color = "black")
plt.axvline(1/10**(((float)(general_cluster_df.iloc[0])+5)/5), color="black",linestyle="--")

x = np.linspace(parallax.min(),parallax.max(),211)
normdist = norm.pdf(x, mean, std)*size*(parallax.max()-parallax.min())/n_bins
plt.plot(x, normdist, color = 'red')
plt.fill_between(x, normdist, 0, where = (x >= mean-std) & (x <= mean+std), alpha=0.4, color = 'red')
plt.fill_between(x, normdist, 0, where = (x >= mean-2*std) & (x <= mean+2*std), alpha=0.2, color = 'red')

plt.text(-0.00075, 26, "NGC 6569", fontsize=14, verticalalignment='top')
# plt.text(0.00027, 3, r'$+\sigma$', color='red', fontsize=10, weight='bold')
# plt.text(-0.0001, 3, r'$-\sigma$', color='red', fontsize=10, weight='bold')

plt.show()