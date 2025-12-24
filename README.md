# Statistical Distribution Analysis of Student Heights

## Overview
This project performs a statistical analysis of height data collected from high school students.
The goal is to examine the distributional properties of the data and determine whether common probability distributions adequately model it, using formal hypothesis testing rather than assumptions.

## Objectives
* Analyze the statistical characteristics of height data
* Explore the data using descriptive statistics and visualization
* Test whether the data follows Normal or Log-normal distributions
* Draw statistically justified conclusions

## Dataset
* Variable: Height of high school students
* Type: Continuous numerical variable
* Measurement scale: Ratio

## Methodology
1. **Explicit data understanding**
   Initial expectations and assumptions were documented prior to analysis.

2. **Descriptive statistics**
   Mean, variance, standard deviation, skewness, and kurtosis were computed and interpreted.

3. **Exploratory data analysis**
   Histograms, empirical PDFs, and box plots were used to understand the data shape and spread.

4. **Hypothesis testing**
   Formal hypothesis tests were conducted at a 5% significance level to evaluate:
   * Normal distribution
   * Log-normal distribution
     Q–Q plots and goodness-of-fit tests were used for validation.

## Results
* Normal distribution: Rejected at the 5% significance level
* Log-normal distribution: Rejected at the 5% significance level
The data exhibits mild right skewness and lighter tails compared to a Normal distribution.

## Conclusion
The height data does not conform well to either Normal or Log-normal distributions.
This suggests that the data may arise from heterogeneous sub-populations or may not be well represented by a single parametric distribution.

## Repository Structure
statistical-distribution-analysis/
├── explicit_info.md
├── descriptive_stats.md
├── hypothesis_test.md
├── exploratory_visualization.ipynb
├── hs_heights.csv
└── README.md

## Tools Used
* Python
* NumPy
* Pandas
* SciPy
* Matplotlib
