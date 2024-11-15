import pandas as pd
from scipy.stats import f_oneway
import scipy.stats as stats
import numpy as np

def __effect_size(sample1: pd.Series, sample2: pd.Series):
    '''
    Calculate the Effect Size (Eta Squared) between two samples.
    '''
    total_sample = pd.concat([sample1, sample2])

    return total_sample.mean()/(np.sqrt(2)*total_sample.std())


def test_report(sample1: pd.Series, sample2: pd.Series, 
                outcome_label : str, predictor_1_label :str, 
                predictor_2_label : str):

    f_stat, pvalue = f_oneway(sample1, sample2)


    if pvalue < 0.05:
        print(f'''
            An independent-samples t-test was run to determine if there
            were differences in {outcome_label} for {predictor_1_label} and
            {predictor_2_label}. The {outcome_label} was NOT shown to be statiscally different,
            as the pvalue were found to be {pvalue:.2f}
    ''')
        return

    eff_size = __effect_size(sample1, sample2)

    mean_1 = sample1.mean()
    std_1 = sample1.std()
    mean_2 = sample2.mean()
    std_2 = sample2.std()

    if mean_1>mean_2:
        ci_1, ci_2 = stats.t.interval(0.95, len(sample1)-1, loc=mean_1, scale=stats.sem(sample1))

        print(f'''
            An independent-samples t-test was run to determine if there
            were differences in {outcome_label} for {predictor_1_label} and
            {predictor_2_label}. The {outcome_label} was shown to be higher
            for {predictor_1_label} (M = {mean_1:.2f}, SD = {std_1:.2f}) than for 
            {predictor_2_label} (M = {mean_2:.2f}, SD = {std_2:.2f}), a statistically significant
            difference, M = {mean_1-mean_2:.2f}, 95% CI[{ci_1:.2f}-{ci_2:.2f}], 
            t({len(sample1)}) = {f_stat:.2f}, p = {pvalue:.2f}, d ={eff_size:.2f}.
    ''')
        
    else:
        ci_1, ci_2 = stats.t.interval(0.95, len(sample2)-1, loc=mean_2, scale=stats.sem(sample2))

        print(f'''
            An independent-samples t-test was run to determine if there
            were differences in {outcome_label} for {predictor_1_label} and
            {predictor_2_label}. The {outcome_label} was shown to be higher
            for {predictor_2_label} (M = {mean_2:.2f}, SD = {std_2:.2f}) than for 
            {predictor_1_label} (M = {mean_1:.2f}, SD = {std_1:.2f}), a statistically significant
            difference, M = {mean_2-mean_1:.2f}, 95% CI[{ci_1:.2f}-{ci_2:.2f}], 
            t({len(sample2)}) = {f_stat:.2f}, p = {pvalue:.2f}, d ={eff_size:.2f}.
    ''')
