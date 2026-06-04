import pandas as pd

df = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")

print(df.head())

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nAge Groups:")
print(df["age_group"].value_counts())

print("\nGender:")
print(df["gender"].value_counts())