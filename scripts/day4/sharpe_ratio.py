import pandas as pd
import numpy as np

returns_df = pd.read_csv(
    "data/processed/daily_returns.csv"
)

returns_df = returns_df.dropna()

risk_free_rate = 0.065

results = []

for fund in returns_df["amfi_code"].unique():

    fund_returns = returns_df[
        returns_df["amfi_code"] == fund
    ]["daily_return"]

    annual_return = (
        fund_returns.mean() * 252
    )

    annual_volatility = (
        fund_returns.std() * np.sqrt(252)
    )

    sharpe_ratio = (
        (annual_return - risk_free_rate)
        / annual_volatility
    )

    results.append([
        fund,
        round(sharpe_ratio, 4)
    ])

sharpe_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "sharpe_ratio"
    ]
)

sharpe_df = sharpe_df.sort_values(
    "sharpe_ratio",
    ascending=False
)

print(sharpe_df.head())

sharpe_df.to_csv(
    "data/processed/sharpe_ratio.csv",
    index=False
)

print("\nSharpe Ratio Saved Successfully!")