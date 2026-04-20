import pandas as pd
from scipy.stats import chi2_contingency

# Load dataset
df = pd.read_csv("labeled_dataset.csv")

# Contingency table
table = pd.crosstab(df["Category"], df["Performance_Label"])

# Chi-square test
stat, p, dof, exp = chi2_contingency(table)

print("Chi-Square Test")
print("p-value =", p)

if p < 0.05:
    print("Category and Performance are related")
else:
    print("No significant relation")