import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw/05_category_inflows.csv")

# Convert month
df["month"] = pd.to_datetime(df["month"])

# Pivot table
heatmap_data = df.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

# Plot
plt.figure(figsize=(16,8))

sns.heatmap(
    heatmap_data,
    cmap="YlGnBu",
    linewidths=0.5
)

plt.title("Category Net Inflow Heatmap")
plt.xlabel("Month")
plt.ylabel("Fund Category")

plt.tight_layout()

plt.savefig("reports/category_heatmap.png")

plt.show()

print("Heatmap Saved Successfully!")