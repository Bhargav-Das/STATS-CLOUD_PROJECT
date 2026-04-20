import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("labeled_dataset.csv")

# Graph 1 Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Load Time(s)"], bins=20)
plt.title("Load Time Distribution")
plt.xlabel("Load Time(s)")
plt.ylabel("Frequency")
plt.savefig("graph1.png")
plt.close()

# Graph 2 Bar Chart
avg = df.groupby("Performance_Label")["Throughput"].mean()

plt.figure(figsize=(8,5))
avg.plot(kind="bar")
plt.title("Average Throughput by Performance")
plt.ylabel("Throughput")
plt.savefig("graph2.png")
plt.close()

# Graph 3 Pie Chart
df["Performance_Label"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Performance Label Distribution")
plt.ylabel("")
plt.savefig("graph3.png")
plt.close()

print("Graphs saved successfully")