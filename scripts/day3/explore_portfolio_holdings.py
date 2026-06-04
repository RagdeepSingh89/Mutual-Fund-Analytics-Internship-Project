import pandas as pd

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

print(df.head())
print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)