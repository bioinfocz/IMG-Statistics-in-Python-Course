# --- Exercise 02 ---
# Fit a linear model: height ~ bmi
import statsmodels.formula.api as smf
from statsmodels.stats.diagnostic import het_white, het_breuschpagan

model = smf.ols(formula='height ~ bmi', data=df)
results = model.fit()
y_predict = results.predict(df)

# 1. Print the summary
print(results.summary())

# 2. Residual diagnostics
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
sns.scatterplot(x=y_predict, y=results.resid, ax=ax[0])
ax[0].axhline(0, color='red')
ax[0].set_xlabel('Predicted')
ax[0].set_ylabel('Residuals')
sns.histplot(results.resid, ax=ax[1])
ax[1].set_xlabel('Residuals')
plt.tight_layout()
plt.show()

# 3. White's test
LMstat, LMpval, Fstat, Fpval = het_white(results.resid, model.data.exog)
print('White test p-value:', LMpval)

# --- Bonus: add shoe_size as a second predictor ---
model2 = smf.ols(formula='height ~ bmi + shoe_size', data=df)
results2 = model2.fit()
y_predict2 = results2.predict(df)

print('\n--- Bonus model: height ~ bmi + shoe_size ---')
print(results2.summary())
print('R2_a (bmi only):         {:.3f}'.format(results.rsquared_adj))
print('R2_a (bmi + shoe_size):  {:.3f}'.format(results2.rsquared_adj))
