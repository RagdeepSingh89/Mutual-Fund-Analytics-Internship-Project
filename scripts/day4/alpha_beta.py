import pandas as pd
import numpy as np
from scipy.stats import linregress

returns_df = pd.read_csv(
    "data/processed/daily_returns.csv"
)

returns_df = returns_df.dropna()

results = []

for fund in returns_df["amfi_code"].unique():

    fund_returns = returns_df[
        returns_df["amfi_code"] == fund
    ]["daily_return"]

    benchmark_returns = returns_df[
        returns_df["amfi_code"] == fund
    ]["daily_return"].rolling(20).mean()

    temp = pd.DataFrame({
        "fund": fund_returns,
        "benchmark": benchmark_returns
    }).dropna()

    if len(temp) < 30:
        continue

    slope, intercept, r_value, p_value, std_err = linregress(
        temp["benchmark"],
        temp["fund"]
    )

    beta = slope

    alpha = intercept * 252

    results.append([
        fund,
        round(alpha, 4),
        round(beta, 4)
    ])

alpha_beta_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "alpha",
        "beta"
    ]
)

alpha_beta_df = alpha_beta_df.sort_values(
    "alpha",
    ascending=False
)

print(alpha_beta_df.head())

alpha_beta_df.to_csv(
    "data/processed/alpha_beta.csv",
    index=False
)

print("\nAlpha Beta Saved Successfully!")