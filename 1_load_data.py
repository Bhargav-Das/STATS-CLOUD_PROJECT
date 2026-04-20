import pandas as pd

df = pd.read_csv("labeled_dataset.csv")

print("Dataset Loaded Successfully")
print(df.head())
print(df.columns)
print(df.shape)