df_num = df[num_columns]

sns.clustermap(df_num.corr(),
               figsize=(10,10),
               z_score=None,
               row_cluster=True,
               col_cluster=True,
               method='ward',
               cmap='coolwarm',vmax=1,vmin=-1, 
               annot=True, annot_kws={"size": 13},cbar_kws={"label": 'Pearson\ncorrelation'})
## representing the categorical variables
fig, axes = plt.subplots( 2,3 , figsize = (15,8) )


sns.violinplot(y='gender',x='height',data=df , 
               color="0.8", inner = 'stick', ax=axes[0,0])

sns.violinplot(y='smoker_nonsmoker',x='height',data=df , 
               color="0.8", inner = 'stick', ax=axes[0,1] )

sns.violinplot(y='birth_place',x='height',data=df , 
               color="0.8", inner = 'stick', ax=axes[0,2] )

sns.violinplot(y='hair_colour',x='height',data=df ,
               color="0.8", inner = 'stick', ax=axes[1,0] )

sns.violinplot(y='eye_colour',x='height',data=df ,
               color="0.8", inner = 'stick', ax=axes[1,1] )

sns.violinplot(y='diet',x='height',data=df , order = [1,2,3,4],
               color="0.8", inner = 'stick', ax=axes[1,2] )

fig.tight_layout()

#Not normal (do the normality test if you want). So no t test. Let's go for non parametric

stat , pval =  stats.mannwhitneyu( df.height[df.gender=='M'] , 
                               df.height[df.gender=='F']  )
print('Mann-Whitney rank test p-value for gender :' , pval)


stat , pval =  stats.mannwhitneyu( df.height[df.smoker_nonsmoker=='NS'] , 
                               df.height[df.smoker_nonsmoker=='S']  )
print('Mann-Whitney rank test p-value for smoker :' , pval)



#birth_place: many under-represented labels 

# no ANOVA for us here, so we replace it with a Kruskal-Wallis test. 
# H1 is a significant association of the factor with a change in the average of the numerical variable

print('Kruskal-Wallis test for hair colour')
s,pval = stats.kruskal(df.height[df.hair_colour=='lb'] , df.height[df.hair_colour=='db'], df.height[df.hair_colour=='bl'])
print('\t\t->',pval)

print('Kruskal-Wallis test for eye colour')
s,pval = stats.kruskal(df.height[df.eye_colour=='1'] , df.height[df.eye_colour=='2'], df.height[df.eye_colour=='3'], df.height[df.eye_colour=='4'])
print('\t\t->',pval)

print('Kruskal-Wallis test for diet')
s,pval = stats.kruskal(df.height[df.diet=='1'] , df.height[df.diet=='2'], df.height[df.diet=='3'], df.height[df.diet=='4'])
print('\t\t->',pval)
