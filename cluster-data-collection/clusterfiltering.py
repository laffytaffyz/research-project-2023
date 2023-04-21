import pandas as pd, os, numpy as np, matplotlib.pyplot as plt, operator

directory = "C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\Data (Other Versions)\\Final Original Cluster Data"

for files in os.listdir(directory):
    if files.find("-Gaia_2MASS.csv") >= 0:
        cluster_name = files[:files.index("-Gaia_2MASS.csv")]
        print(cluster_name)
        cluster_df = pd.read_csv(directory + "\\" + files)
        
        general_clusters_df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\final general cluster data.csv")
        general_clusters_df.set_index("GES_FLD", inplace = True)
        general_cluster_df = general_clusters_df.loc[cluster_name]

        # filtering based on parallax data
        parallax = cluster_df['parallax']
        pmean = parallax.mean()
        pstd = parallax.std()
        distance_modulus = general_cluster_df.iloc[0]
        accepted_parallax = 1000/(10**((distance_modulus+5)/5))

        if ((parallax + pstd < accepted_parallax) or (parallax - pstd > accepted_parallax)):
            print("***INCONSISTENT PARALLAX", cluster_name)
