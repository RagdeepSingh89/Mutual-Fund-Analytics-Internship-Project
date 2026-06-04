import pandas as pd

df = pd.read_csv("data/raw/05_category_inflows.csv")

print(df.head())
print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)