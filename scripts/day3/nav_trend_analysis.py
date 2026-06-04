import pandas as pd
import plotly.express as px

# Load cleaned NAV data
df = pd.read_csv("data/processed/02_nav_history_cleaned.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create line chart
fig = px.line(
    df,
    x="date",
    y="nav",
    color="amfi_code",
    title="Daily NAV Trend (2022-2026)"
)

# Highlight 2023 Bull Run
fig.add_vrect(
    x0="2023-01-01",
    x1="2023-12-31",
    fillcolor="green",
    opacity=0.15,
    annotation_text="2023 Bull Run",
    annotation_position="top left"
)

# Highlight 2024 Market Correction
fig.add_vrect(
    x0="2024-01-01",
    x1="2024-12-31",
    fillcolor="red",
    opacity=0.10,
    annotation_text="2024 Correction",
    annotation_position="top left"
)

# Save chart
fig.write_html("reports/nav_trend.html")

# Save chart
fig.write_html("reports/nav_trend.html")

# Display chart
fig.show()

print("Chart Saved Successfully!")