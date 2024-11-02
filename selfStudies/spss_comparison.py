# %%
'''
I've checked that possibly SPSS and Python gives differents answers for some descriptive statistics. Let's check this out with fake data.
'''
import numpy as np
import pandas as pd
from scipy.stats import skew
from statsmodels.stats.stattools import robust_skewness


df = pd.read_csv('testdata.csv', sep=',', decimal='.')
scipy_skew = skew(df['X'])
stats_models = robust_skewness(df['X'])



# %%
