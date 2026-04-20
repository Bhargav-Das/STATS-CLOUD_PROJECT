import pandas as pd
from scipy.stats import ttest_ind

# Load dataset
df = pd.read_csv("labeled_dataset.csv")

# Clean text values
df["Performance_Label"] = df["Performance_Label"].str.lower().str.strip()

# Two groups
fast = df[df["Performance_Label"] == "fast"]["Load Time(s)"]
slow = df[df["Performance_Label"] == "slow"]["Load Time(s)"]

# T-test
stat, p = ttest_ind(fast, slow)

print("T-Test Result")
print("p-value =", p)

if p < 0.05:
    print("Significant difference in Load Time between Fast and Slow websites")
else:
    print("No significant difference")