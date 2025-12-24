import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv("hs_heights.csv")
heights = data["heights"]

mean_height = heights.mean()
std_height = heights.std()
median_height = heights.median()
skewness = stats.skew(heights)
kurtosis = stats.kurtosis(heights)
max_height = heights.max()
min_height = heights.min()

print("Mean = ",mean_height)
print("Standard deviation = ",std_height)
print("Median = ",median_height)
print("Skewness = ",skewness)
print("Kurtosis = ",kurtosis)
print("Max Height = ",max_height)
print("Min Height = ",min_height)