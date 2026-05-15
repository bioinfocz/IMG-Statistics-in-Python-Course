## HELP
## 1. How likely was this result, provided the coin is fair? 

# Save the experiment distribution to make it more readable
experiment_distrib = stats.binom(n= ... ,p= ... )

# Probability of this result
proba_7 = experiment_distrib.pmf( ... )
print(f"The probability of obtaining heads 7 times is {proba_7}\n\n")

## Solution :
# %load -r 1-13 solutions/solution_02_02.py



#----------------------------------------------------------------------------
## HELP
## 2. How likely was it to come up with at most 7 heads, provided the coin is fair? 
#     getting at most 7 = pobability of getting 0, or 1, or 2, or ..., or 7

# one (tedious) possibility:
# experiment_distrib.pmf(0) + experiment_distrib.pmf(1) + experiment_distrib.pmf(2) + ... 

# better: Use Cumulative Distribution Function -> sum of probability of everything before and including a given number 
proba = ...
print(f"The probability of obtaining 7 heads or less is : {proba}")

## Solution :
# %load -r 18-27 solutions/solution_02_02.py



#----------------------------------------------------------------------------
## HELP
## 3. How likely was it to come up with at least 7 heads, provided the coin is fair? 

# Use Cumulative Distribution Function
# hint : the probability to get 7 heads or more is the probability of NOT doing 6 or less 
proba = ...
print(f"The probability of obtaining 7 heads or more is : {proba}")

## Solution :
# %load -r 32-37 solutions/solution_02_02.py



#----------------------------------------------------------------------------
## HELP
## 4. How likely was it to come up with a result at least as far from the expected mean of 5, provided the coin is fair? 
#     results at least as extreme as 7 are : 0,1,2,3 and 7,8,9,10

proba_3_or_fewer = ...
proba_7_or_more  = ...
proba            = ...

print(f"The probability of obtaining a result at least as extreme as 7 is : {proba}")

## Solution :
# %load -r 42-50 solutions/solution_02_02.py



#----------------------------------------------------------------------------
## HELP
## 5. How about if you come up with 1 head out of 10 ? Do you think the coin is fair in that case? 

## Compute the 2-sided p-value 
proba_1_or_fewer = ...
proba_9_or_more  = ...
proba            = ...

print(f"The probability of obtaining a result at least as extreme as 1 head (p-value) is: {proba}")

## Conclusion
# Hint : What is H0 here ? Is the p-value < 0.05 ? 

## Solution :
# %load -r 55- solutions/solution_02_02.py
