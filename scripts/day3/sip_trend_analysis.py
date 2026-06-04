import pandas as pd
import plotly.express as px

# Load SIP inflow data
df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print(df.head())
print("\nColumns:")
print(df.columns)

# Convert month
df["month"] = pd.to_datetime(df["month"])

# Plot
fig = px.line(
    df,
    x="month",
    y="sip_inflow_crore",
    title="Monthly SIP Inflows (2022-2025)"
)

# Annotate Dec 2025 high
peak = df.loc[df["sip_inflow_crore"].idxmax()]

fig.add_annotation(
    x=peak["month"],
    y=peak["sip_inflow_crore"],
    text=f"All Time High ₹{peak['sip_inflow_crore']:,.0f} Cr",
    showarrow=True
)

fig.write_html("reports/sip_trend.html")

fig.show()

print("SIP Trend Saved Successfully!")