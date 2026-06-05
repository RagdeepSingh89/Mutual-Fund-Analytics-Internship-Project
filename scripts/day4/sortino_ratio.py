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

    downside_returns = fund_returns[
        fund_returns < 0
    ]

    downside_std = (
        downside_returns.std()
        * np.sqrt(252)
    )

    sortino_ratio = (
        (annual_return - risk_free_rate)
        / downside_std
    )

    results.append([
        fund,
        round(sortino_ratio, 4)
    ])

sortino_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "sortino_ratio"
    ]
)

sortino_df = sortino_df.sort_values(
    "sortino_ratio",
    ascending=False
)

print(sortino_df.head())

sortino_df.to_csv(
    "data/processed/sortino_ratio.csv",
    index=False
)

print("\nSortino Ratio Saved Successfully!")