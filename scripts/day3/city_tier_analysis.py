import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")

tier_counts = df["city_tier"].value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    tier_counts,
    labels=tier_counts.index,
    autopct="%1.1f%%"
)

plt.title("T30 vs B30 Investor Distribution")

plt.savefig("reports/city_tier_distribution.png")

plt.show()

print("City Tier Chart Saved!")