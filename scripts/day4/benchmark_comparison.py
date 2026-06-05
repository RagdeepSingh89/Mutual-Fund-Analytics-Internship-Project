import pandas as pd
import plotly.express as px

# Load NAV data
nav_df = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

# Load scorecard
scorecard_df = pd.read_csv(
    "data/processed/fund_scorecard.csv"
)

# Top 5 funds
top_funds = (
    scorecard_df
    .sort_values("score", ascending=False)
    .head(5)["amfi_code"]
)

comparison_df = nav_df[
    nav_df["amfi_code"].isin(top_funds)
].copy()

comparison_df["date"] = pd.to_datetime(
    comparison_df["date"]
)

fig = px.line(
    comparison_df,
    x="date",
    y="nav",
    color="amfi_code",
    title="Top 5 Funds Benchmark Comparison"
)

fig.show()

# Save html version
fig.write_html(
    "reports/benchmark_comparison.html"
)

print(
    "\nBenchmark Comparison Chart Saved Successfully!"
)