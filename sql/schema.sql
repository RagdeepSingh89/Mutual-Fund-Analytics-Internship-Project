-- Dimension Table

CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    amfi_code INTEGER UNIQUE,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    risk_grade TEXT
);

-- Date Dimension

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

-- NAV Fact

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    nav REAL,

    FOREIGN KEY (fund_id)
    REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
    REFERENCES dim_date(date_id)
);

-- Transactions Fact

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    transaction_type TEXT,
    amount_inr REAL,

    FOREIGN KEY (fund_id)
    REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
    REFERENCES dim_date(date_id)
);

-- Performance Fact

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    fund_id INTEGER,

    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,

    sharpe_ratio REAL,
    sortino_ratio REAL,
    expense_ratio_pct REAL,

    FOREIGN KEY (fund_id)
    REFERENCES dim_fund(fund_id)
);

-- AUM Fact

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    aum_crore REAL,

    FOREIGN KEY (fund_id)
    REFERENCES dim_fund(fund_id)
);