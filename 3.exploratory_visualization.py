import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

data = pd.read_csv("hs_heights.csv")
heights = data["heights"]

#Histogram
plt.hist(heights, bins=15, color="Orange",edgecolor="black")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.title("Histogram of High School Students' Heights")
plt.show()

#Pdf(Empirical)
kde = gaussian_kde(heights)
x = np.linspace(heights.min(), heights.max(), 200)
plt.plot(x, kde(x))
plt.xlabel("Height")
plt.ylabel("Density")
plt.title("Empirical PDF using KDE")
plt.show()