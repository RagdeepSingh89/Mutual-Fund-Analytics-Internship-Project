import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

# Ensure returns are numeric
for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Flag anomalies
df["anomaly_flag"] = False

for col in return_cols:
    df.loc[
        (df[col] < -100) |
        (df[col] > 100),
        "anomaly_flag"
    ] = True

# Validate expense ratio
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

# Remove duplicates
before = len(df)

df = df.drop_duplicates()

after = len(df)

print("Duplicates Removed:", before - after)

# Save cleaned dataset
df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)

print("\nAnomalies Found:")
print(df["anomaly_flag"].value_counts())

print("\nExpense Ratio Summary:")
print(df["expense_ratio_pct"].describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFile Saved Successfully!")