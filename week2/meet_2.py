
# %%
def filter_rows(x):
    try:
        float(x)
        return True
    except:
        return False


import os
import pandas as pd
path = os.path.join(os.getcwd(), 'datasets','Titanic.csv')
dataset = pd.read_csv(path, sep=',', decimal='.')


dataset
# %%
