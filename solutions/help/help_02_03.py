## HELP
## 1. Compute the effect size of the diet on the weight of mice

##-- Part 1 : Get sample means
mean_CHOW = np.mean()
mean_HFD  = np.mean()

##-- Part 2 : Get the standard deviation
## When comparing two samples, we need a single estimate of the standard deviation.
## The correct approach is to pool the two sample variances : https://en.wikipedia.org/wiki/Pooled_variance
## This corresponds to a weighted average of the sample variances

n_CHOW = ...    # Sample size
n_HFD  = ...

variance_CHOW   = np.var( ... , ddof= ... )  # Remember that the denominator of the sample variance is n-1
variance_HFD    = np.var( ... , ddof= ... ) 
variance_pooled = ((variance_CHOW * (n_CHOW-1)) + (variance_HFD * (n_HFD-1))) / (n_CHOW + n_HFD - 2) # This is a weighted average
std_pooled      = ...    # Compute standard deviation

##-- Part 3 : From there, the effect size can be computed as before:
effect_size = ...
print(f"Effect size of diet on mouse weight: {effect_size:.4f}")

## Solution :
# %load -r 1-23 solutions/solution_02_03.py



#----------------------------------------------------------------------------
## HELP
## 2. Compute the statistical power of the corresponding t-test for that effect size (with significance level = 0.05)

P = TTestIndPower()
power = P.power(effect_size= ... , nobs1= ... , ratio= ... , alpha= ... )
print(f"Statistical power of the t-test : {power}")

## Solution :
# %load -r 28- solutions/solution_02_03.py
