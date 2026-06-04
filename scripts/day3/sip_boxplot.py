import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")

sip_df = df[df["transaction_type"] == "Sip"]

plt.figure(figsize=(10,6))

sns.boxplot(
    x="age_group",
    y="amount_inr",
    data=sip_df
)

plt.title("SIP Amount Distribution by Age Group")

plt.xlabel("Age Group")
plt.ylabel("Investment Amount (INR)")

plt.tight_layout()

plt.savefig("reports/sip_boxplot.png")

plt.show()

print("Boxplot Saved!")