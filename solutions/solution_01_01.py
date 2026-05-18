
# 1. Select towns with less than 1000 inhabitants, or with more than 1 Foreigner. How many such towns are there?


mask=( df['Total']<1000 ) | ( df['Foreigner']>0 ) 
print( "there are" ,mask.sum() , "towns with less than 1000 inhabitants, or more than 1 Foreigner." )
# applying sum on a set of False/True make them behave like 0/1. Thus the sum is the number of True.


#2. Create a new column is the `DataFrame` representing the fraction of population which is Reformed in each town.


df['fraction reformed'] = df['Reformed']/df['Total']
print( df['fraction reformed'].head()  )

# What is the minimum/maximum value for this fraction?

print( 'minimum:' , df['fraction reformed'].min())
print( 'maximum:' , df['fraction reformed'].max())

#3. How many towns conforming condition 1. while having at least 99% Reformed are in the dataset?

mask2 = mask & (df['fraction reformed']>=0.99)
print( "there are" ,mask2.sum() , "towns with less than 1000 inhabitants, or more than 1 Foreigner and at least 99% of Reformed" )

# 4. Which columns contain zeros (value of 0) and how many appearances of 0 do you observe in each column like that? Anything worth investigating here?

for x in df.columns:
    if sum(df[x]==0) > 0:
        print('# zeros in column',x,':',sum(df[x]==0))