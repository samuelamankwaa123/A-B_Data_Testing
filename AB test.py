import pandas as pd
from scipy.stats import ttest_ind

# Load the data
data = pd.read_csv('C:/Users/kasutaja/Desktop/ab_test_data.txt', delimiter=',')


# Calculate conversion rates for each group
conversion_rates = data.groupby('Group')['Converted'].mean()
print("Conversion Rates by Group:")
print(conversion_rates)

# Separate the data into the two groups
group_a = data[data['Group'] == 'A']['Converted']
group_b = data[data['Group'] == 'B']['Converted']

# Perform a t-test to see if the difference is statistically significant
t_stat, p_value = ttest_ind(group_a, group_b, equal_var=False)

print("\nT-test Results:")
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Interpret the result
alpha = 0.05
if p_value < alpha:
    print("\nResult: Statistically significant difference in conversion rates.")
else:
    print("\nResult: No statistically significant difference in conversion rates.")
