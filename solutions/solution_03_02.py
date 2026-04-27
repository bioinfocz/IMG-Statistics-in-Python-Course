wt = mice_data[mice_data.genotype == 'WT']['weight']
ko = mice_data[mice_data.genotype == 'KO']['weight']

ksStat, pvalue = stats.ks_2samp(wt, ko)
print('1-sample Kolmogorov-Smirnov test:')
print('KS test statistic :', ksStat)
print('p-value :', pvalue)