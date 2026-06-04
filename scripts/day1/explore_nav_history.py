import pandas as pd

df = pd.read_csv("data/processed/02_nav_history_cleaned.csv")

print(df.columns)
print(df.head())