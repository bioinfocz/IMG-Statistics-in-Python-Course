f=sns.catplot( x = '60+ y.o.', y= 'canton name' ,
             data=dfFractions , kind = 'box' , orient='h',height=5.0, aspect=1.40 )
plt.grid()

# save PDF, dimensions follow plot
f.savefig('./exC.pdf')

# save PNG with dpi parameter
#f.savefig('./exC.png',dpi=150)
