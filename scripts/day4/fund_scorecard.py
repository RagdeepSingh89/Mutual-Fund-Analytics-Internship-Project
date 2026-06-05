import pandas as pd

cagr_df = pd.read_csv(
    "data/processed/cagr_table.csv"
)

sharpe_df = pd.read_csv(
    "data/processed/sharpe_ratio.csv"
)

alpha_df = pd.read_csv(
    "data/processed/alpha_beta.csv"
)

mdd_df = pd.read_csv(
    "data/processed/max_drawdown.csv"
)

scorecard = (
    cagr_df
    .merge(sharpe_df, on="amfi_code")
    .merge(alpha_df, on="amfi_code")
    .merge(mdd_df, on="amfi_code")
)

scorecard["cagr_rank"] = (
    scorecard["cagr_pct"]
    .rank(ascending=False)
)

scorecard["sharpe_rank"] = (
    scorecard["sharpe_ratio"]
    .rank(ascending=False)
)

scorecard["alpha_rank"] = (
    scorecard["alpha"]
    .rank(ascending=False)
)

scorecard["mdd_rank"] = (
    scorecard["max_drawdown_pct"]
    .rank(ascending=False)
)

n = len(scorecard)

scorecard["score"] = (
    (1 - scorecard["cagr_rank"]/n) * 30 +
    (1 - scorecard["sharpe_rank"]/n) * 25 +
    (1 - scorecard["alpha_rank"]/n) * 20 +
    (1 - scorecard["mdd_rank"]/n) * 25
)

scorecard = scorecard.sort_values(
    "score",
    ascending=False
)

print(
    scorecard[
        ["amfi_code","score"]
    ].head()
)

scorecard.to_csv(
    "data/processed/fund_scorecard.csv",
    index=False
)

print(
    "\nFund Scorecard Saved Successfully!"
)