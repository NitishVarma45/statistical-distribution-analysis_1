import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("hs_heights.csv")
heights = data["heights"]

#Q-Q Plot
stats.probplot(heights, dist="norm", plot=plt)
plt.title("Q-Q Plot for Height Data")
plt.show()

#The plot shows that the points are deviating at a place, which doesn't make the given data normally distributed.

#KS test
mu = heights.mean()
sigma = heights.std(ddof=1)
ks_stat, p_value = stats.kstest(heights, 'norm', args=(mu, sigma))
print("KS Statistic:", ks_stat)
print("p-value:", p_value)

#p-value ~ 0, clearly the given data does not follow Normal distribution