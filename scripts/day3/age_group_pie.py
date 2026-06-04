import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")

age_counts = df["age_group"].value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    age_counts,
    labels=age_counts.index,
    autopct="%1.1f%%"
)

plt.title("Investor Age Group Distribution")

plt.savefig("reports/age_group_distribution.png")

plt.show()

print("Age Group Pie Chart Saved!")