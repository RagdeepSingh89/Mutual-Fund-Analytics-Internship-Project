import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")

sip_df = df[df["transaction_type"].str.lower() == "sip"]

state_amount = (
    sip_df.groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12,6))

sns.barplot(
    x=state_amount.index,
    y=state_amount.values
)

plt.title("Total SIP Amount by State")
plt.xlabel("State")
plt.ylabel("Total SIP Amount (INR)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/state_distribution.png")

plt.show()

print("State Distribution Chart Saved!")