## First, a little plot to meet the data:
fig, axes = plt.subplots(1, 3, figsize=(15,5), sharey=True)

sns.histplot(y=df['weightDiff'], kde=True, ax = axes[0])
sns.rugplot(y=df['weightDiff'], ax = axes[0])
sns.violinplot(x='Diet', y='weightDiff', data=df, ax = axes[1])
sns.boxplot(x='Diet', y='weightDiff', data=df, fill=False, showmeans=True, ax = axes[2])
plt.show()
## Test the assumptions for ANOVA:
# QQplots
fig, axes = plt.subplots(1, 3, figsize=(15,5), sharey=True)

# There are 3 levels of diet: 1, 2, and 3
for i, diet in enumerate([1,2,3]):
    stats.probplot(df.loc[df.Diet == diet, 'weightDiff'], plot=axes[i])
    axes[i].set_title("diet " + str(diet))
plt.show()

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
groups = [
          df['weightDiff'][df['Diet'] == 1], 
          df['weightDiff'][df['Diet'] == 2],
          df['weightDiff'][df['Diet'] == 3]
]

Fstat, pval = stats.f_oneway(*groups)

print('Automated One-way ANOVA / F-test:')
print('F-stat: ', Fstat)
print('p-value: ', pval)

if pval < 0.05:
    # statistical significance should be accompanied by actual effect size:
    print('Mean weightloss per group:')
    print(df.groupby('Diet')['weightDiff'].mean())
# ANOVA showed a significant result, so we can now perform Tukey's HSD:
hsd_res = stats.tukey_hsd(*groups)

print(hsd_res)

labels = ['1 vs 2', '1 vs 3', '2 vs 3']
pairs = [(1,2), (1,3), (2,3)]

ci = hsd_res.confidence_interval(confidence_level=0.95)
means  = [hsd_res.statistic[i-1][j-1] for i, j in pairs]
lows   = [ci.low[i-1][j-1]  for i, j in pairs]
highs  = [ci.high[i-1][j-1] for i, j in pairs]

err_low  = [m - l for m, l in zip(means, lows)]
err_high = [h - m for h, m in zip(highs, means)]

colors = ['red' if l > 0 or h < 0 else 'steelblue' for l, h in zip(lows, highs)]

fig, ax = plt.subplots(figsize=(8,4))
for idx, (m, el, eh, c) in enumerate(zip(means, err_low, err_high, colors)):
    ax.errorbar(m, idx, xerr=[[el], [eh]], fmt='o', color=c, ecolor=c, elinewidth=2, capsize=5)

ax.axvline(0, color='grey', linestyle='--')
ax.set_yticks(range(len(pairs)))
ax.set_yticklabels(labels)
ax.set_xlabel('Mean Difference')
ax.set_title('Tukey HSD — 95% Confidence Intervals')
plt.tight_layout()
plt.show()