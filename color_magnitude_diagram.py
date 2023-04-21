import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    ax.scatter(x, y, s=5,alpha=0.5)

    # now determine nice limits by hand:
    xbinwidth = 0.05
    ybinwidth = 0.25

    # bins = np.arange(-lim, lim + binwidth, binwidth)
    xbins = np.arange(np.min(x), np.max(x), xbinwidth)
    # ybins = np.arange(-(int(abs(np.min(y))/ybinwidth) + 1) * ybinwidth, (int(abs(np.max(y))/ybinwidth) + 1) * ybinwidth, ybinwidth)
    ybins = np.arange(np.min(y), np.max(y), ybinwidth)
    ax_histx.hist(x, bins=xbins)
    ax_histy.hist(y, bins=ybins, orientation='horizontal')

directory = "C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\Revised Gaia 2MASS Data"

# for files in os.listdir(directory):
#     cluster_name = files[:files.index("-result.csv")]
#     print(cluster_name)
cluster_name = "Br32"
df = pd.read_csv(directory + "\\" + cluster_name + "-result.csv")

general_clusters_df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\final general cluster data.csv")
general_clusters_df.set_index("GES_FLD", inplace = True)
general_cluster_df = general_clusters_df.loc[cluster_name]

reddening = 0.52*(float)(general_cluster_df.iloc[6])
appcolor = df['j_m'] - (df["ks_m"] + 0.044)
color = df['j_m'] - (df["ks_m"] + 0.044) - reddening

extinction = 0.3584*(float)(general_cluster_df.iloc[6])
appmag = df["ks_m"] + 0.044
mag = (df["ks_m"]  + 0.044) + 5 -5*np.log10(1000/df['parallax']) - extinction

fig = plt.figure()
gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4), wspace=0.05, hspace=0.05)
ax = fig.add_subplot(gs[1, 0])
ax.set_xlabel(r'$(J-K)_0$')
ax.set_ylabel(r'$M_K$')

ax.invert_yaxis()
ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)

ax.text(0.05, 0.95, cluster_name, transform=ax.transAxes, fontsize=14, verticalalignment='top')
scatter_hist(color, mag,ax,ax_histx,ax_histy)

# rect = patches.Rectangle((0.92, -2.7), 0.3, 0.6, linewidth=1, edgecolor='r', facecolor='none')
# ax.add_patch(rect)

# checking RC in the CMDs
rcdf = pd.read_csv('C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\Red Clump Cluster Data\\' + cluster_name + '-red clump.csv')
rccolor = rcdf['j_m'] - (rcdf["ks_m"] + 0.044) - reddening
rcmag = (rcdf["ks_m"]  + 0.044) + 5 -5*np.log10(1000/rcdf['parallax']) - extinction
# ax.scatter(color,mag,s=5,alpha=0.5)
ax.scatter(rccolor, rcmag,s=5,alpha=0.5)
ax.set_title('Color-Magnitude Diagram of ' + cluster_name, pad = 70)
plt.show()