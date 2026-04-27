## First, a little plot to meet the data:
fig, axes = plt.subplots(1, 2, figsize=(14,7), sharey=True)

sns.histplot(y=df['weightDiff'], kde=True, ax = axes[0])
sns.rugplot(y=df['weightDiff'], ax = axes[0])
sns.violinplot(x='Diet', y='weightDiff', data=df, ax = axes[1])
## Test the assumptions for ANOVA:
# QQplots
fig, axes = plt.subplots(1, 3, figsize=(14,7), sharey=True)

# There are 3 levels of diet: 1, 2, and 3
for i, diet in enumerate([1,2,3]):
    stats.probplot(df.loc[df.Diet == diet, 'weightDiff'], plot=axes[i])
    axes[i].set_title("diet " + str(diet))

# Using groupby, we can apply the test function to each condition automatically:
print('Checking the assumptions of ANOVA:')

print('Shapiro-Wilk test of normality...')
print(df.groupby('Diet')['weightDiff'].apply(stats.shapiro))

print('Bartlett test of homoscedasticity...')
stat, pval = stats.bartlett(df['weightDiff'][df['Diet'] == 1], 
                            df['weightDiff'][df['Diet'] == 2],
                            df['weightDiff'][df['Diet'] == 3]
                           )
print('Statistic: ', stat)
print('p-value: ', pval)
# The assumptions seem verified, we can perform the test:
Fstat, pval = stats.f_oneway(df['weightDiff'][df['Diet'] == 1], 
                             df['weightDiff'][df['Diet'] == 2],
                             df['weightDiff'][df['Diet'] == 3]
                            )
print('Automated One-way ANOVA / F-test:')
print('F-stat: ', Fstat)
print('p-value: ', pval)

if pval < 0.05:
    # statistical significance should be accompanied by actual effect size:
    print('Mean weightloss per group:')
    print(df.groupby('Diet')['weightDiff'].mean())