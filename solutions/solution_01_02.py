# 1. plot the distribution of the total number of habitants. Try to choose an appropriate mode of representation (histogram, density line? number of bins?)

## density line: 
#sns.kdeplot(df['Total'] )

## log-transform the data, use more bins
sns.histplot(np.log10(df['Total']) , kde=True, bins=100)

# 2. try to call `sns.histplot` twice in a row, once with to plot the fraction of Foreigner and the other for the fraction of Swiss. What happens?

sns.histplot(dfFractions['Swiss'] , kde=False)
sns.histplot(dfFractions['Foreigner'] , kde=False)


# 3. plot the distribution of the fraction of catholics in the canton of Zurich.

maskZH = dfFractions['canton'] == 'ZH'
sns.histplot(dfFractions.loc[maskZH,'Catholic'])