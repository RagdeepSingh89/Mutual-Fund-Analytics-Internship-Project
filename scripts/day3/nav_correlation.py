import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/processed/02_nav_history_cleaned.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Select first 10 funds
top_funds = df["amfi_code"].unique()[:10]

df = df[df["amfi_code"].isin(top_funds)]

# Create pivot table
pivot_df = df.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

# Daily returns
returns = pivot_df.pct_change().dropna()

# Correlation matrix
corr_matrix = returns.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("NAV Return Correlation Matrix")
plt.tight_layout()

plt.savefig("reports/nav_correlation.png")

plt.show()

print("Correlation Matrix Saved Successfully!")