import pandas as pd

df = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")

print(df[["state", "city_tier", "amount_inr"]].head())

print("\nStates:")
print(df["state"].value_counts())

print("\nCity Tier:")
print(df["city_tier"].value_counts())