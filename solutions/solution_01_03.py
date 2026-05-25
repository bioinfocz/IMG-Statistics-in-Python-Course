plt.rc("font", size=10)
f, axes = plt.subplots( 1, 2, figsize=(10, 7) )
sns.boxplot( x = '60+ y.o.', y= 'canton name' ,data=dfFractions , color="royalblue",ax=axes[0]).set_title('(A) 60+ y.o. per canton')
axes[0].axvline(dfFractions['60+ y.o.'].mean(),color='g', linestyle='--' , label = "mean")
axes[0].legend()
sns.histplot( hue = 'majority language' , x='Catholic' , data=dfFractions, multiple='dodge', ax=axes[1])
axes[1].set_title('(B) Catholic prop. per language')
sns.move_legend(axes[1], "upper right")
plt.tight_layout()# this makes the panels margins and setup more graceful

# save PDF, dimensions follow plot
f.savefig('./exC.pdf')

# save PNG with dpi parameter
#f.savefig('./exC.png',dpi=150)
