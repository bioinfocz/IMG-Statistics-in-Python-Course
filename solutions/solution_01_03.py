f, axes = plt.subplots( 1, 2, figsize=(10, 7) )
sns.boxplot( x = '60+ y.o.', y= 'canton name' ,data=dfFractions , ax=axes[0]).set_title('(A) 60+ y.o. per canton')
sns.histplot( hue = 'majority language' , x='Catholic' , data=dfFractions, multiple='dodge', ax=axes[1]).set_title('(B) Catholic prop. per language')
plt.tight_layout()# this makes the panels margins and setup more graceful


# save PDF, dimensions follow plot
f.savefig('./exC.pdf')

# save PNG with dpi parameter
#f.savefig('./exC.png',dpi=150)
