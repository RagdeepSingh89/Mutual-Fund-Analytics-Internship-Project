-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average 1 Year Return

SELECT
    AVG(return_1yr_pct) AS avg_return_1yr
FROM fact_performance;


-- 3. Average 3 Year Return

SELECT
    AVG(return_3yr_pct) AS avg_return_3yr
FROM fact_performance;


-- 4. Average 5 Year Return

SELECT
    AVG(return_5yr_pct) AS avg_return_5yr
FROM fact_performance;


-- 5. Funds with Expense Ratio < 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 6. Highest Sharpe Ratio Funds

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;


-- 7. Highest Sortino Ratio Funds

SELECT
    scheme_name,
    sortino_ratio
FROM fact_performance
ORDER BY sortino_ratio DESC
LIMIT 5;


-- 8. Funds by Risk Grade

SELECT
    risk_grade,
    COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;


-- 9. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 10. Total Investment Amount by Transaction Type

SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;