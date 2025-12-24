import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("hs_heights.csv")
heights = data["heights"]

#Q-Q Plot
log_heights = np.log(heights)
stats.probplot(log_heights, dist="norm", plot=plt)
plt.title("Q-Q Plot of log(Height)")
plt.show()

#Not a straight Line.

#KS Test
mu_log = log_heights.mean()
sigma_log = log_heights.std(ddof=1)
ks_stat, ks_p = stats.kstest(
    log_heights,
    'norm',
    args=(mu_log, sigma_log)
)
print("KS p-value:", ks_p)

#p-value is still low(~0), So most likely not Lognormal distribution.