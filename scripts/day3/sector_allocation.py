import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

# Aggregate sector weights
sector_weights = (
    df.groupby("sector")["weight_pct"]
    .sum()
    .sort_values(ascending=False)
)

# Plot donut chart
plt.figure(figsize=(10, 8))

plt.pie(
    sector_weights,
    labels=sector_weights.index,
    autopct="%1.1f%%",
    startangle=90
)

# Create donut hole
centre_circle = plt.Circle((0, 0), 0.65, fc="white")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Sector Allocation Across Equity Funds")

plt.tight_layout()

plt.savefig("reports/sector_allocation.png")

plt.show()

print("Sector Allocation Chart Saved Successfully!")