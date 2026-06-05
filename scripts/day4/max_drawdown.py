import pandas as pd

nav_df = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

nav_df["date"] = pd.to_datetime(nav_df["date"])

results = []

for fund in nav_df["amfi_code"].unique():

    fund_df = nav_df[
        nav_df["amfi_code"] == fund
    ].copy()

    fund_df = fund_df.sort_values("date")

    fund_df["running_max"] = (
        fund_df["nav"].cummax()
    )

    fund_df["drawdown"] = (
        fund_df["nav"] /
        fund_df["running_max"] - 1
    )

    max_dd = fund_df["drawdown"].min()

    worst_row = fund_df.loc[
        fund_df["drawdown"].idxmin()
    ]

    results.append([
        fund,
        round(max_dd * 100, 2),
        worst_row["date"]
    ])

mdd_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "max_drawdown_pct",
        "worst_date"
    ]
)

mdd_df = mdd_df.sort_values(
    "max_drawdown_pct"
)

print(mdd_df.head())

mdd_df.to_csv(
    "data/processed/max_drawdown.csv",
    index=False
)

print("\nMaximum Drawdown Saved Successfully!")