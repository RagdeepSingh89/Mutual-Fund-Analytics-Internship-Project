import pandas as pd

nav_df = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)

results = []

for fund in nav_df["amfi_code"].unique():

    fund_df = nav_df[
        nav_df["amfi_code"] == fund
    ]

    start_nav = fund_df.iloc[0]["nav"]
    end_nav = fund_df.iloc[-1]["nav"]

    years = (
        (fund_df.iloc[-1]["date"] -
         fund_df.iloc[0]["date"]).days
    ) / 365

    cagr = (
        (end_nav / start_nav) ** (1 / years) - 1
    ) * 100

    results.append([
        fund,
        round(cagr, 2)
    ])

cagr_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "cagr_pct"
    ]
)

cagr_df = cagr_df.sort_values(
    "cagr_pct",
    ascending=False
)

print(cagr_df.head())

cagr_df.to_csv(
    "data/processed/cagr_table.csv",
    index=False
)

print("\nCAGR Table Saved Successfully!")