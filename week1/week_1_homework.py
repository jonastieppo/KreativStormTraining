#  Importanting the dataset

# %%
import os
import pandas as pd
path = os.path.join(os.getcwd(), 'datasets','Birthweight.csv')
dataset = pd.read_csv(path, sep=',', decimal='.')

dataset
# %%
