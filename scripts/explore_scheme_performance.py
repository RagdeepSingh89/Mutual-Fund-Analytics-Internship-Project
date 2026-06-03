import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print(df.head())

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nShape:")
print(df.shape)