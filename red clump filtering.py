
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import os

# loading directory with all the crossmatched cluster red clump data 
# and creating empty final cluster red clump data for regression analysis 
directory = "C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\Final Red Clump Cluster Data"
rcdf = pd.DataFrame({'GES_FLD': pd.Series(dtype='str'),
                   'MK': pd.Series(dtype='float'),
                   'J-K': pd.Series(dtype='float'),
                   'Age': pd.Series(dtype='float'),
                   'FeH': pd.Series(dtype='float')})

for files in os.listdir(directory):
    # loading data
    cluster_name = files[:files.index("-final red clump.csv")]
    df = pd.read_csv(directory + "\\" + cluster_name + "-final red clump.csv")
    general_clusters_df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\final general cluster data.csv")
    general_clusters_df.set_index("GES_FLD", inplace = True)
    general_cluster_df = general_clusters_df.loc[cluster_name]

    # filtering with cuts from Bovy et al. (2014)
    df = df.dropna()
    df = df[(df['LOGG'] >= 1.8) & (df['LOGG'] <= 0.0018*(df['TEFF'] - (-382.5*df['FEH'].mean() + 4607)) + 2.5)]
    reddening = 0.52*(float)(general_cluster_df.iloc[6])
    df = df[df['FEH'] <= 0.06]
    df = df[(df['j_m'] - df["ks_m"] - reddening) >= 0.5]
    print(cluster_name, df)

    # obtaining mean values
    color = (df['j_m'] - (df["ks_m"] + 0.0044) - reddening).mean()

    extinction = 0.3584*(float)(general_cluster_df.iloc[6])
    mag = ((df["ks_m"]  + 0.044) + 5 -5*np.log10(1000/df['parallax']) - extinction).mean()

    age = general_cluster_df.iloc[5]
    feh = df['FEH'].mean()

    df.to_csv('C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\Filtered Final Red Clump Cluster Data\\' + cluster_name + '-filtered final red clump.csv')

    # adding data to final cluster red clump data for regression analysis
    tempdf = pd.DataFrame([[cluster_name, mag, color, age, feh]], columns=['GES_FLD','MK','J-K','Age','FeH'])
    rcdf = pd.concat([rcdf, tempdf],ignore_index=True)
    
rcdf.to_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\red clump.csv")
