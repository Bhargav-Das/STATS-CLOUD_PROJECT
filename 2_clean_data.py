import pandas as pd

df = pd.read_csv("labeled_dataset.csv")

print("Before Cleaning:", df.shape)

df = df.drop_duplicates()
df = df.dropna()

print("After Cleaning:", df.shape)
print(df.head())
