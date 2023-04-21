# 1.8 ≤ log g ≤ 0.0018(T_eff - T_eff^ref([Fe/H])) where T_eff^ref([Fe/H]) = -382.5[Fe/H] + 4607
# [Fe/H] > 1.21[(J-K_S)_0 - 0.05]^9 + 0.0011 (6)
# [Fe/H] < 2.58[(J-K_S)_0 - 0.40]^3 + 0.0034 (7)
# [Fe/H] ≤ 0.06 and (J-K_S)_0 ≥ 0.5 (8)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import os

df = pd.read_csv("C:\\Users\\tiffa\\Downloads\\2022-2023 HSR\\red clump.csv")
print("mean", df['MK'].mean())
print("std", df['MK'].std())
