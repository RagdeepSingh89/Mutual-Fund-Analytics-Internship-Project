import pandas as pd

# Load data
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# 1. Fix date format
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# 2. Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only valid transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]

df = df[df["transaction_type"].isin(valid_types)]

# 3. Validate amount > 0
df = df[df["amount_inr"] > 0]

# 4. Standardize KYC status
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.title()
)

valid_kyc = ["Verified", "Pending"]

df = df[df["kyc_status"].isin(valid_kyc)]

# 5. Remove duplicates
before = len(df)

df = df.drop_duplicates()

after = len(df)

print("Duplicates Removed:", before - after)

# Save cleaned file
df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTransaction Types:")
print(df["transaction_type"].value_counts())

print("\nKYC Status:")
print(df["kyc_status"].value_counts())

print("\nFile Saved Successfully!")