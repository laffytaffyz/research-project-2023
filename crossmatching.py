# crossmatching GES and Gaia data
# since GES already classified Trumpler 20 stars, data from Gaia will 
# be added onto GES data when applicable

import numpy as np
import pandas as pd
import math
import os

directory = "C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\Red Clump Cluster Data"
destination_directory = "C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\Final Red Clump Cluster Data"

for files in os.listdir(directory):
    cluster_name = files[:files.index("-red clump.csv")]
    rc_df = pd.read_csv(directory + "\\" + cluster_name + '-red clump.csv')

    # loading ges data
    ges_df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\Data (Other Versions)\\Final Original Cluster Data\\" + cluster_name + "-GES.csv")

    # list of columns to be added
    object_list = list()
    ges_fld_list = list()
    teff_list = list()
    e_teff_list = list()
    logg_list = list()
    e_logg_list = list()
    feh_list = list()
    e_feh_list = list()

    count = 0

    for index, row in rc_df.iterrows():
        rc_ra = row['ra']
        rc_dec = row['dec']
        rc_ra_error = row['ra_error']
        rc_dec_error = row['dec_error']

        # default values for columns to be added
        object = np.nan
        ges_fld = np.nan
        teff = np.nan
        e_teff = np.nan
        logg = np.nan
        e_logg = np.nan
        feh = np.nan
        e_feh = np.nan

        closest_adist = 10 # in radians so largest is pi

        for index, row in ges_df.iterrows():
            ges_ra = row['RA']
            ges_dec = row['DECLINATION']
            ges_error = 0.025

            if (min(ges_ra + ges_error, rc_ra + rc_ra_error) >= max (ges_ra - ges_error, rc_ra - rc_ra_error) 
                and min(ges_dec + ges_error, rc_dec + rc_dec_error) >= max (ges_dec - ges_error, rc_dec - rc_dec_error)):
                cos_adist = math.sin(ges_dec*math.pi/180)*math.sin(rc_dec*math.pi/180)+math.cos(ges_dec*math.pi/180)*math.cos(rc_dec*math.pi/180)*math.cos((ges_ra-rc_ra)*math.pi/180)
                adist = math.acos(cos_adist)

                # updating column value for the row when applicable
                if adist < closest_adist:
                    closest_adist = adist

                    object = (str)(row['OBJECT'])
                    ges_fld = (str)(row['GES_FLD'])
                    teff = (float)(row['TEFF'])
                    e_teff = (float)(row['E_TEFF'])
                    logg = (float)(row['LOGG'])
                    e_logg = (float)(row['E_LOGG'])
                    feh = (float)(row['FEH'])
                    e_feh = (float)(row['E_FEH'])
                
        # adding column value for the row
        object_list.append(object)
        ges_fld_list.append(ges_fld)
        teff_list.append(teff)
        e_teff_list.append(e_teff)
        logg_list.append(logg)
        e_logg_list.append(e_logg)
        feh_list.append(feh)
        e_feh_list.append(e_feh)

        print(count, cluster_name)
        count += 1

    # adding columns
    rc_df = rc_df.assign(OBJECT = object_list)
    rc_df = rc_df.assign(GES_FLD = ges_fld_list)
    rc_df = rc_df.assign(TEFF = teff_list)
    rc_df = rc_df.assign(E_TEFF = e_teff_list)
    rc_df = rc_df.assign(LOGG = logg_list)
    rc_df = rc_df.assign(E_LOGG = e_logg_list)
    rc_df = rc_df.assign(FEH = feh_list)
    rc_df = rc_df.assign(E_FEH = e_feh_list)

    rc_df.to_csv(destination_directory + "\\" + cluster_name + "-final red clump.csv")