import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")

gender_counts = df["gender"].value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct="%1.1f%%"
)

plt.title("Gender Distribution")

plt.savefig("reports/gender_distribution.png")

plt.show()

print("Gender Chart Saved!")