import pandas as pd, math

# all the metallicity-luminosity relations
def youngiband(feh):
    return 0.6496*feh + 0.5056

def alliband(feh):
    return 0.5916*feh + 0.4649

def oldkband(feh):
    return -0.2254*feh + -1.6033

# loading and processing the data for each of the relations
df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\i-band and k-band red clump.csv")
idf = df[df['mi'].notna()]
iyoungdf = idf.drop(idf[idf['age (gyr)']>2].index)
iolddf = idf.drop(idf[idf['age (gyr)']<2].index)
kdf = df[df['mk'].notna()]
kolddf = kdf.drop(kdf[kdf['age (gyr)']<2].index)

predicted_youngiband_mag = youngiband(iyoungdf['feh'])
predicted_alliband_mag = alliband(idf['feh'])
predicted_oldiband_mag = alliband(iolddf['feh']) 
predicted_oldkband_mag = oldkband(kolddf['feh'])

# calculating the RMS for each of predicted magnitudes from the relations
iyoungrms = math.sqrt((((iyoungdf['mi']-predicted_youngiband_mag)**2).sum())/len(iyoungdf['mi']-predicted_youngiband_mag))
irms = math.sqrt((((idf['mi']-predicted_alliband_mag)**2).sum())/len(idf['mi']-predicted_alliband_mag))
ioldrms = math.sqrt((((iolddf['mi']-predicted_oldiband_mag)**2).sum())/len(iolddf['mi']-predicted_oldiband_mag))
koldrms = math.sqrt((((kolddf['mk']-predicted_oldkband_mag)**2).sum())/len(kolddf['mk']-predicted_oldkband_mag))

print('Young I-band RMS magnitude:', iyoungrms)
print('All I-band RMS magnitude:', irms)
print('Old I-band from All I-band relation RMS magnitude:', ioldrms)
print('Old K-band RMS magnitude:', koldrms)

# calculating the RMS for each of the predicted distances from the relations
predicted_youngiband_distance = iyoungdf['app_mi']-predicted_youngiband_mag
predicted_alliband_distance = idf['app_mi']-predicted_alliband_mag
predicted_oldiband_distance = iolddf['app_mi']-predicted_oldiband_mag
predicted_oldkband_distance = kolddf['app_mk']-predicted_oldkband_mag

iyoungrms = math.sqrt((((iyoungdf['m-M']-predicted_youngiband_distance)**2).sum())/len(iyoungdf['m-M']-predicted_youngiband_distance))
irms = math.sqrt((((idf['m-M']-predicted_alliband_distance)**2).sum())/len(idf['m-M']-predicted_alliband_distance))
ioldrms = math.sqrt((((iolddf['m-M']-predicted_oldiband_distance)**2).sum())/len(iolddf['m-M']-predicted_oldiband_distance))
koldrms = math.sqrt((((kolddf['m-M']-predicted_oldkband_distance)**2).sum())/len(kolddf['m-M']-predicted_oldkband_distance))

print('Young I-band RMS:', iyoungrms)
print("Percent RMS:", math.sqrt(((((iyoungdf['m-M']-predicted_youngiband_distance)/predicted_youngiband_distance)**2).sum())/len(iyoungdf['m-M']-predicted_youngiband_distance)))
print('All I-band RMS:', irms)
print("Percent RMS:", math.sqrt(((((idf['m-M']-predicted_alliband_distance)/predicted_alliband_distance)**2).sum())/len(idf['m-M']-predicted_alliband_distance)))
print('Old I-band from All I-band relation RMS:', ioldrms)
print("Percent RMS:", math.sqrt(((((iolddf['m-M']-predicted_oldiband_distance)/predicted_oldiband_distance)**2).sum())/len(iolddf['m-M']-predicted_oldiband_distance)))
print('Old K-band RMS:', koldrms)
print("Percent RMS:", math.sqrt(((((kolddf['m-M']-predicted_oldkband_distance)/predicted_oldkband_distance)**2).sum())/len(kolddf['m-M']-predicted_oldkband_distance)))

# calculating the RMS of the average distances predicted from the I-band relation of all of the RC and K-band relation of old RC
predicted_kandirelation_avg_distance = pd.concat([predicted_oldiband_distance, predicted_oldkband_distance], axis=1).dropna()
predicted_kandirelation_avg_distance = (predicted_kandirelation_avg_distance[0]+predicted_kandirelation_avg_distance[1])/2
kandirelation_df = df[df['mi'].notna() & df['mk'].notna() & (df['age (gyr)'] > 2)]
kandirelation_avg_rms = math.sqrt((((kandirelation_df['m-M']-predicted_kandirelation_avg_distance)**2).sum())/len(kandirelation_df['m-M']-predicted_kandirelation_avg_distance))
print('I-band and K-band Relation Average RMS:', kandirelation_avg_rms)
print("Percent RMS:", math.sqrt(((((kandirelation_df['m-M']-predicted_kandirelation_avg_distance)/predicted_kandirelation_avg_distance)**2).sum())/len(kandirelation_df['m-M']-predicted_kandirelation_avg_distance)))

# calculating the RMS of the distances predicted from the average I-band magnitude, from the average K-band magnitude, and from the average of both their predicted distances
mean_rc_i = -0.516
mean_rc_k = -1.580

predicted_i_distance = iolddf['app_mi']-mean_rc_i
predicted_k_distance = kolddf['app_mk']-mean_rc_k

irms = math.sqrt((((iolddf['m-M']-predicted_i_distance)**2).sum())/len(iolddf['m-M']-predicted_i_distance))
krms = math.sqrt((((kolddf['m-M']-predicted_k_distance)**2).sum())/len(kolddf['m-M']-predicted_k_distance))

print('Mean I-band RMS:', irms)
print("Percent RMS:", math.sqrt(((((iolddf['m-M']-predicted_i_distance)/predicted_i_distance)**2).sum())/len(iolddf['m-M']-predicted_i_distance)))
print('Mean K-band RMS:', krms)
print("Percent RMS:", math.sqrt(((((kolddf['m-M']-predicted_k_distance)/predicted_k_distance)**2).sum())/len(kolddf['m-M']-predicted_k_distance)))

predicted_kandi_avg_distance = pd.concat([predicted_i_distance, predicted_k_distance], axis=1).dropna()
predicted_kandi_avg_distance = (predicted_kandi_avg_distance['app_mi']+predicted_kandi_avg_distance['app_mk'])/2
kandi_df = df[df['mi'].notna() & df['mk'].notna()]
predicted_kandi_avg_rms = math.sqrt((((kandi_df['m-M']-predicted_kandi_avg_distance)**2).sum())/len(kandi_df['m-M']-predicted_kandi_avg_distance))

print('Mean I-band and K-band Average RMS', predicted_kandi_avg_rms)
print("Percent RMS:", math.sqrt(((((kandi_df['m-M']-predicted_kandi_avg_distance)/predicted_kandi_avg_distance)**2).sum())/len(kandi_df['m-M']-predicted_kandi_avg_distance)))
