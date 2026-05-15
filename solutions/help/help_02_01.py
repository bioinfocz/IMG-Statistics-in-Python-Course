## HELP

## 1. What would be the normal law followed by the mean of this sample of size 10 according to the CLT ? 

#- Write your answer here :

## According to the CLT, the mean of this sample follows a normal distribution with the parameters :
mean = ...
std  = ...


#- Plot the corresponding pdf :

fig, ax = plt.subplots(1, figsize=(7,7)) # Create the figure
x = np.linspace( ... ) # Create x axis
y = stats.norm.pdf(x= ... , loc= ... , scale= ... ) # Create y axis
sns.lineplot( ... , ax=ax) # plot the curve
plt.title( ... ) # title of the figure
ax.set_ylabel( ... ) # label of y axis
ax.set_xlabel( ... ) # label of x axis
plt.show()

## Solution :
# %load -r 1-21 solutions/solution_02_01.py



#----------------------------------------------------------------------------
## HELP
## 2. Do you think a sample size of 10 is large enough for the CLT to apply ?
## Let's make a simulation to decide - simulate multiple coin toss experiments and plot a histogram of the distribution of the sample means
## Then compare this distribution with theoretical values

#- You can use this function to simulate the result of n coin toss experiment

def sampling_mean(sample_size=10, p=0.5):
    """ Returns the proportion of heads — equivalent to the sample mean of 'sample_size' Bernoulli trials """
    sample_mean = sum(np.random.random(sample_size) > p) / sample_size 
    return sample_mean

#- Simulate multiple coin toss experiments and save the means in a list/array 

n = 10000         # Number of simulations
sample_size = 10  # Sample size
p = 0.5           # Probability of success

list_sample_means = []
for i in range( ... ):
    sample_mean = ...  # Simulate one experiment
    list_sample_means.append( ... ) # Store the results



#- Plot the results of the simulation in a histogram


fig, ax = plt.subplots(figsize=(14, 7))

bins = np.linspace(0-(0.5/sample_size), 1+(0.5/sample_size), sample_size + 2) #  sample_size + 2 bins centered on each possible value (e.g. 0/10, 1/10, ..., 10/10 for sample_size = 10)

sns.histplot( ... , label= ... , bins=bins, stat="density", ax=ax)



#- Plot the expected pdf according to the CLT
## Re-use your code from the previous question


mean = ...
std  = ...
x = np.linspace(0, 1, 100)
y = stats.norm.pdf(x= ... , loc= ... , scale= ... )
sns.lineplot(x= ... , y= ... , label= ... , color="orange", ax=ax)



#- Plot the true pdf/pmf of the binomial distribution 

theoretical_binomial = stats.binom(n=sample_size, p=p)
sns.scatterplot(x=np.arange(sample_size+1)/sample_size, y=theoretical_binomial.pmf(np.arange(sample_size+1))*sample_size, label = 'actual binomial distribution', ax=ax, s=100, color='green')


#- Name axes and plot

ax.set_title( ... )
ax.set_ylabel( ... )
ax.set_xlabel( ... )

plt.show()


#- Conclusion

# What do you think, does your simulated distribution and the CLT prediction match the real distribution pmf ?



## Solution :
# %load -r 26- solutions/solution_02_01.py
