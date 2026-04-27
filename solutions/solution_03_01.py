## Chi-squared test
chi2, pval, df, expected = stats.chi2_contingency(table, correction=False)
print("Chi-squared test")
print('\tchi2:', chi2)
print('\tp-value:', pval)

## Fisher's exact test
oddsratio, pvalue = stats.fisher_exact(table)
print("Fisher's exact test")
print('\todds ratio:', oddsratio)
print('\tp-value:', pvalue)

## Both tests can be used here. 
## Fisher's will be more accurate but more computationally expensive; on the other hand, 
## Chi-squared will be quicker, computationally less expensive, but only approximate, not exact.