import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print(df.head())
print(df.columns)

# Create chart
# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Extract year
df["year"] = df["date"].dt.year

plt.figure(figsize=(14,8))

sns.barplot(
    data=df,
    x="year",
    y="aum_crore",
    hue="fund_house"
)

plt.title("AUM Growth by Fund House (2022-2025)")
plt.xlabel("Year")
plt.ylabel("AUM (Crore)")

plt.tight_layout()

plt.savefig("reports/aum_growth.png")

plt.show()

print("Chart Saved Successfully!")