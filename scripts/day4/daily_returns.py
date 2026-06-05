import pandas as pd

nav_df = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)

nav_df["daily_return"] = (
    nav_df.groupby("amfi_code")["nav"]
    .pct_change()
)

print(nav_df.head())

print("\nShape:")
print(nav_df.shape)

nav_df.to_csv(
    "data/processed/daily_returns.csv",
    index=False
)

print("\nDaily Returns Saved Successfully!")