from scipy.stats import shapiro, monte_carlo_test
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def shapiro_test(Y_var : pd.Series):

    def shapiro_stats(x):
        return shapiro(x).statistic

    ML_data = monte_carlo_test(Y_var, rvs=st.norm.rvs, 
                            statistic=shapiro_stats, alternative='less')
    fig, ax = plt.subplots()
    bins = np.linspace(0.65, 1, 50)
    ax.hist(ML_data.null_distribution, density=True, bins=bins)
    ax.axvline(ML_data.pvalue, label=f'p-value={ML_data.pvalue:.3f}')
    ax.legend(loc='upper left')
    if ML_data.pvalue>0.05:
        ax.annotate('As p-value is greater than 5%, \n it is normally distributed.', xy=(ML_data.pvalue*1.2, 15))
        print('As p-value is greater than 5%, \n it is normally distributed.')
    else:
        ax.annotate('As p-value is lower than 5%, \n it is NOT normally distributed.', xy=(ML_data.pvalue*1.2, 15))
        print('As p-value is lower than 5%, \n it is NOT normally distributed.')