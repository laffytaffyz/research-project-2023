import os, pandas as pd, numpy as np, math

directory = "C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\Revised Gaia 2MASS Data"
destination_directory = "C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\Red Clump Cluster Data"

for files in os.listdir(directory):
    cluster_name = files[:files.index("-result.csv")]
    print(cluster_name)
    df = pd.read_csv(directory + "\\" + cluster_name + '-result.csv')

    general_red_clump_df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\red clump cmd ranges.csv")
    general_red_clump_df.set_index("GES_FLD", inplace = True)
    general_red_clump_df = general_red_clump_df.loc[cluster_name]

    general_clusters_df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\final general cluster data.csv")
    general_clusters_df.set_index("GES_FLD", inplace = True)
    general_cluster_df = general_clusters_df.loc[cluster_name]

    color_lower_bound = (float)(general_red_clump_df.iloc[0])
    color_upper_bound = (float)(general_red_clump_df.iloc[1])
    mag_lower_bound = (float)(general_red_clump_df.iloc[2])
    mag_upper_bound = (float)(general_red_clump_df.iloc[3])

    reddening = 0.52*(float)(general_cluster_df.iloc[6])
    extinction = 0.3584*(float)(general_cluster_df.iloc[6])

    color = df['j_m'] - (df["ks_m"] + 0.044) - reddening
    mag = (df["ks_m"]  + 0.044) + 5 -5*np.log10(1000/(df['parallax'])) - extinction
    red_clump_df = df[(color > color_lower_bound) & (color < color_upper_bound) & (mag > mag_lower_bound) & (mag < mag_upper_bound)]

    red_clump_df.to_csv(destination_directory + '\\' + cluster_name + "-red clump.csv")

