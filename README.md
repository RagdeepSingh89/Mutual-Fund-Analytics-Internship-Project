# 📊 Bluestock MF Analytics — Mutual Fund Analytics Dashboard

> **Bluestock Fintech · Data Analytics Internship · Capstone Project · June 2026**

[![Version](https://img.shields.io/badge/version-v1.0-blue)](https://github.com/RagdeepSingh89/Mutual-Fund-Analytics-Internship-Project/releases/tag/v1.0)
[![Python](https://img.shields.io/badge/python-3.11-green)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)
[![Status](https://img.shields.io/badge/status-complete-brightgreen)]()

---

## 🗂️ Table of Contents

- [Project Overview](#project-overview)
- [Real Data Highlights](#real-data-highlights)
- [Repository Structure](#repository-structure)
- [Dataset Descriptions](#dataset-descriptions)
- [Setup Instructions](#setup-instructions)
- [How to Run the ETL Pipeline](#how-to-run-the-etl-pipeline)
- [How to Open the Dashboard](#how-to-open-the-dashboard)
- [Key Findings (From Real Data)](#key-findings-from-real-data)
- [Team](#team)

---

## 📌 Project Overview

End-to-end Mutual Fund Analytics platform for the Indian market, built during a 7-day internship at Bluestock Fintech. Starting from real AMFI API and industry data, it delivers:

- Automated **ETL pipeline** ingesting NAV, AUM, SIP, folio, and investor transaction data
- **SQLite database** (`bluestock_mf.db`) as single source of truth
- **EDA** across 12 categories, 10 AMCs, and 4-year time horizon (2022–2026)
- Six **risk-adjusted performance metrics** per fund (Sharpe, Sortino, Alpha, Beta, Max Drawdown, CAGR)
- Four **interactive dashboard panels** (Performance, SIP Trends, Industry Overview, Investor Analytics)
- **Final Report PDF** (15+ pages) and **12-slide PPTX presentation** — all values from real data

---

## 📊 Real Data Highlights

> All numbers below come directly from the uploaded datasets — nothing is assumed.

| Metric | Value | Source |
|--------|-------|--------|
| Total Schemes Analysed | 40 | `01_fund_master.csv` |
| Fund Houses | 10 | `01_fund_master.csv` |
| Categories | 12 | `07_scheme_performance_cleaned.csv` |
| Total Industry AUM (Dec 2025) | **₹62.74 Lakh Crore** | `03_aum_by_fund_house.csv` |
| SIP Inflow — Jan 2022 | ₹11,517 Cr | `04_monthly_sip_inflows.csv` |
| SIP Inflow — Dec 2025 (Peak) | **₹31,002 Cr** | `04_monthly_sip_inflows.csv` |
| Total Folios — Jan 2022 | 13.26 Crore | `06_industry_folio_count.csv` |
| Total Folios — Dec 2025 | **26.12 Crore** | `06_industry_folio_count.csv` |
| Avg Sharpe Ratio (40 schemes) | **1.36** | `07_scheme_performance_cleaned.csv` |
| Avg Sortino Ratio (40 schemes) | **2.08** | `07_scheme_performance_cleaned.csv` |
| Avg Alpha (40 schemes) | **1.25** | `07_scheme_performance_cleaned.csv` |
| Avg Beta (40 schemes) | **0.87** | `07_scheme_performance_cleaned.csv` |
| Best 3-Yr Return (Category) | **Small Cap: 21.69%** | `07_scheme_performance_cleaned.csv` |
| Worst Max Drawdown | **−33.5%** (SBI Small Cap Direct) | `max_drawdown.csv` |
| Top CAGR (single scheme) | **32.8%** (ICICI Pru Midcap) | `cagr_table.csv` |
| Investor Age (largest group) | **26–35 yrs (41.1%)** | `08_investor_transactions_cleaned.csv` |
| Gender split | **Male 66.5% / Female 33.5%** | `08_investor_transactions_cleaned.csv` |
| City Tier | **T30: 66.3% / B30: 33.7%** | `08_investor_transactions_cleaned.csv` |
| Transaction split | **Lumpsum 58.49%** / Redemption 35.34% / SIP 6.17% | `08_investor_transactions_cleaned.csv` |
| Top Sector (Portfolio) | **Banking 19.2%** | `09_portfolio_holdings.csv` |

---

## 📁 Repository Structure

```
Mutual-Fund-Analytics-Internship-Project/
│
├── data/
│   ├── raw/                              # Raw API responses
│   ├── 01_fund_master.csv                # 40 schemes, 10 AMCs, 12 categories
│   ├── 02_nav_history.csv                # Raw NAV history
│   ├── 02_nav_history_cleaned.csv        # Cleaned NAV (amfi_code, date, nav)
│   ├── 03_aum_by_fund_house.csv          # Quarterly AUM by AMC (2022–2025)
│   ├── 04_monthly_sip_inflows.csv        # 48 months SIP data
│   ├── 05_category_inflows.csv           # Monthly net inflows by category
│   ├── 06_industry_folio_count.csv       # Folio count growth
│   ├── 07_scheme_performance.csv         # Raw performance
│   ├── 07_scheme_performance_cleaned.csv # 40 rows × 20 cols — main analytics file
│   ├── 08_investor_transactions.csv      # Raw transactions
│   ├── 08_investor_transactions_cleaned.csv # Cleaned investor data
│   ├── 09_portfolio_holdings.csv         # Sector allocation
│   ├── 10_benchmark_indices.csv          # Nifty 500 benchmark
│   ├── alpha_beta.csv                    # Per-scheme Alpha & Beta
│   ├── cagr_table.csv                    # CAGR rankings (full NAV history)
│   ├── daily_returns.csv                 # Daily return % per scheme
│   ├── fund_scorecard.csv                # Composite score (CAGR+Sharpe+Alpha+MDD)
│   ├── max_drawdown.csv                  # Max drawdown per scheme
│   ├── sharpe_ratio.csv                  # Sharpe ratio per scheme
│   ├── sortino_ratio.csv                 # Sortino ratio per scheme
│   ├── five_schemes_nav.csv              # Live NAV for 5 key schemes
│   └── live_nav_125497.csv               # Real-time NAV fetch
│
├── notebooks/
│   ├── EDA_Analysis.ipynb                # Full EDA notebook
│   └── Advanced_Analytics.ipynb          # Sharpe, Sortino, Alpha, Beta, MDD, Scorecard
│
├── scripts/
│   ├── run_pipeline.py                   # 🚀 MASTER EXECUTION SCRIPT
│   ├── extract.py                        # AMFI API + industry data extraction
│   ├── transform.py                      # Cleaning, normalisation, feature engineering
│   ├── load.py                           # SQLite upsert loader
│   ├── metrics.py                        # Risk metric computations
│   └── generate_dashboard.py             # Renders 4-panel HTML dashboard
│
├── dashboard/
│   ├── bluestock_mf_dashboard.html       # 📊 Open in browser — no server needed
│   └── Bluestock_MF_Presentation.pptx   # 12-slide presentation (real data)
│
├── reports/
│   ├── Final_Report.pdf                  # 15+ page report (real data)
│   ├── dashobard1.pdf                    # MF Performance Analysis dashboard
│   ├── dashboard2.pdf                    # SIP & Market Trends dashboard
│   ├── dashoboard3.pdf                   # MF Industry Overview dashboard
│   └── dashboard4.pdf                    # Investor Analytics dashboard
│
├── visualizations/
│   ├── age_group_distribution.png        # Pie: 26-35=41.1%, 36-45=24.9%...
│   ├── aum_growth.png                    # AUM by fund house 2022–2025
│   ├── category_heatmap.png              # Category net inflow heatmap
│   ├── city_tier_distribution.png        # T30 66.3% vs B30 33.7%
│   ├── gender_distribution.png           # Male 66.5% / Female 33.5%
│   ├── nav_correlation.png               # NAV return correlation matrix
│   ├── nav_trend.html                    # Interactive NAV trend
│   ├── sector_allocation.png             # Sector allocation donut chart
│   ├── sip_boxplot.png                   # SIP amount by age group
│   ├── sip_trend.html                    # Interactive SIP trend
│   ├── state_distribution.png            # Total SIP by state
│   └── folio_growth.html                 # Interactive folio count growth
│
├── docs/
│   ├── data_dictionary.md                # Column definitions for all datasets
│   ├── data_quality_report.txt           # Day 1 quality check results
│   └── chart_insights.md                 # Written insights per chart
│
├── data/bluestock_mf.db                  # SQLite database (5 tables)
├── requirements.txt
└── README.md
```

---

## 🗄️ Dataset Descriptions

### Core Performance File: `07_scheme_performance_cleaned.csv`
40 rows × 20 columns — the primary analytics file.

| Column | Type | Description |
|--------|------|-------------|
| `amfi_code` | INT | AMFI scheme identifier |
| `scheme_name` | TEXT | Full scheme name |
| `fund_house` | TEXT | AMC (10 unique) |
| `category` | TEXT | SEBI category (12 unique) |
| `plan` | TEXT | Direct / Regular |
| `return_1yr_pct` | FLOAT | 1-year return % |
| `return_3yr_pct` | FLOAT | 3-year return % |
| `return_5yr_pct` | FLOAT | 5-year return % |
| `benchmark_3yr_pct` | FLOAT | Benchmark return % |
| `alpha` | FLOAT | Jensen's Alpha |
| `beta` | FLOAT | Market Beta (vs Nifty 500) |
| `sharpe_ratio` | FLOAT | Sharpe ratio |
| `sortino_ratio` | FLOAT | Sortino ratio |
| `std_dev_ann_pct` | FLOAT | Annualised volatility |
| `max_drawdown_pct` | FLOAT | Max peak-to-trough drawdown |
| `aum_crore` | FLOAT | AUM in ₹ Crore |
| `expense_ratio_pct` | FLOAT | Expense ratio % |
| `morningstar_rating` | INT | 1–5 stars |
| `risk_grade` | TEXT | Moderate / High / Very High / Low / Moderately High |
| `anomaly_flag` | BOOL | True if outlier detected |

### Category Returns Summary (Real)

| Category | Schemes | Avg 3-Yr Return | Avg Sharpe |
|----------|---------|----------------|------------|
| Small Cap | 6 | **21.69%** | 0.87 |
| Mid Cap | 7 | **16.59%** | 0.87 |
| Flexi Cap | 2 | 15.50% | 0.97 |
| Value | 1 | 14.76% | 0.98 |
| Large Cap | 14 | 12.99% | 0.93 |
| ELSS | 1 | 13.58% | 0.80 |
| Index/ETF | 2 | 11.94% | 0.92 |
| Short Duration | 1 | 7.37% | 1.84 |
| Liquid | 3 | 6.33% | 6.33 |
| Gilt | 2 | **5.69%** | 1.43 |

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.11+  ·  pip  ·  Git

### 1. Clone
```bash
git clone https://github.com/RagdeepSingh89/Mutual-Fund-Analytics-Internship-Project.git
cd Mutual-Fund-Analytics-Internship-Project
```

### 2. Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
pandas==2.1.0
numpy==1.25.2
requests==2.31.0
yfinance==0.2.28
pdfplumber==0.10.2
SQLAlchemy==2.0.20
matplotlib==3.7.2
seaborn==0.12.2
plotly==5.17.0
scipy==1.11.2
scikit-learn==1.3.0
Jinja2==3.1.2
tqdm==4.66.1
python-dotenv==1.0.0
```

---

## 🚀 How to Run the ETL Pipeline

```bash
# Full pipeline (Extract + Transform + Load + Metrics)
python scripts/run_pipeline.py --stage all

# Individual stages
python scripts/run_pipeline.py --stage extract
python scripts/run_pipeline.py --stage transform
python scripts/run_pipeline.py --stage load
python scripts/run_pipeline.py --stage metrics
```

### CLI Options
```
--stage         extract | transform | load | metrics | all
--start-date    e.g. --start-date 2022-01-01  (default: 2022-01-01)
--end-date      e.g. --end-date 2025-12-31    (default: today)
--schemes       all | comma-separated AMFI codes
--log-level     DEBUG | INFO | WARNING         (default: INFO)
```

**Expected runtime:** ~10–15 min for 40 schemes. Logs → `logs/pipeline_YYYYMMDD_HHMMSS.log`

---

## 📊 How to Open the Dashboard

```bash
# macOS
open dashboard/bluestock_mf_dashboard.html

# Linux
xdg-open dashboard/bluestock_mf_dashboard.html

# Windows — double-click the file, or:
start dashboard/bluestock_mf_dashboard.html
```

No web server needed — fully self-contained HTML file.

To regenerate from latest database:
```bash
python scripts/generate_dashboard.py
```

### Dashboard Panels

| # | Panel | Key Charts |
|---|-------|------------|
| 1 | MF Performance Analysis | Risk vs Return scatter · Avg 3yr return by category · Top funds table |
| 2 | SIP & Market Trends | SIP vs Nifty 50 line · Category inflow heatmap · Top 5 FY25 categories |
| 3 | MF Industry Overview | KPI cards · AUM by AMC · Industry AUM trend 2022–2025 |
| 4 | Investor Analytics | Transaction by state · Gender/Age/City pie charts · Monthly volume |

---

## 🔍 Key Findings (From Real Data)

1. **Small Cap leads returns** — Avg 3-yr return 21.69% vs Gilt at 5.69% (lowest category)
2. **SIP boom** — Monthly inflows grew 2.7× from ₹11,517 Cr (Jan'22) to ₹31,002 Cr (Dec'25)
3. **Folio count doubled** — 13.26 Crore → 26.12 Crore in just 4 years
4. **AUM concentration** — Top 3 AMCs (SBI, ICICI, HDFC) hold 51.8% of ₹62.74L Cr total AUM
5. **Healthy risk metrics** — Avg Sharpe 1.36, Sortino 2.08 across 40 schemes
6. **True diversification** — Fund NAV correlations range from −0.09 to +0.05 (near-zero)
7. **Young investors dominate** — 26–35 age group = 41.1% of investor base
8. **B30 opportunity** — B30 cities already represent 33.7% of investors

---

**Mentor:** Bluestock Fintech · Data Analytics Division
**Duration:** 7-Day Intensive Capstone · June 2026

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

*Bluestock Fintech Pvt. Ltd. · Data Analytics Division · Capstone v1.0 · June 2026*
*All metrics computed from real AMFI and industry data — no values assumed.*
