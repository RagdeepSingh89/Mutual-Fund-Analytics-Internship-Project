# Mutual Fund Analytics - Data Dictionary

## 02_nav_history_cleaned.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| date | DATE | NAV date |
| nav | FLOAT | Net Asset Value |

---

## 08_investor_transactions_cleaned.csv

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Fund AMFI code |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | FLOAT | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier classification |
| age_group | TEXT | Investor age bracket |
| gender | TEXT | Investor gender |
| annual_income_lakh | FLOAT | Annual income in lakhs |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC verification status |

---

## 07_scheme_performance_cleaned.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Scheme code |
| scheme_name | TEXT | Mutual fund scheme |
| fund_house | TEXT | Fund house name |
| category | TEXT | Fund category |
| plan | TEXT | Direct/Regular plan |
| return_1yr_pct | FLOAT | 1 year return |
| return_3yr_pct | FLOAT | 3 year return |
| return_5yr_pct | FLOAT | 5 year return |
| benchmark_3yr_pct | FLOAT | Benchmark return |
| alpha | FLOAT | Alpha value |
| beta | FLOAT | Beta value |
| sharpe_ratio | FLOAT | Sharpe Ratio |
| sortino_ratio | FLOAT | Sortino Ratio |
| std_dev_ann_pct | FLOAT | Annualized volatility |
| max_drawdown_pct | FLOAT | Maximum drawdown |
| aum_crore | FLOAT | Assets under management |
| expense_ratio_pct | FLOAT | Expense ratio |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk category |