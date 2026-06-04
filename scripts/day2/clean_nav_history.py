import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# 1. Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# 2. Sort by AMFI code and date
df = df.sort_values(
    by=["amfi_code", "date"]
)

# 3. Forward fill missing NAV values
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# 4. Remove duplicates
before = len(df)

df = df.drop_duplicates()

after = len(df)

print("Duplicates Removed:", before - after)

# 5. Keep only valid NAV values
df = df[df["nav"] > 0]

# Save cleaned file
df.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst 5 Rows:")
print(df.head())

print("\nFile Saved Successfully!")