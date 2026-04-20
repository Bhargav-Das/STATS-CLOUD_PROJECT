import pandas as pd

df = pd.read_csv("labeled_dataset.csv")
df = df.dropna()

print(df.describe())