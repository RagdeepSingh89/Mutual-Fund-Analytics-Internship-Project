import pandas as pd
import plotly.express as px

# Generate monthly data from Jan 2022 to Dec 2025

dates = pd.date_range(
    start="2022-01-01",
    end="2025-12-01",
    freq="MS"
)

# Folio count grows from 13.26 Cr to 26.12 Cr

start_folio = 13.26
end_folio = 26.12

folio_counts = []

for i in range(len(dates)):
    value = start_folio + (
        (end_folio - start_folio)
        * i
        / (len(dates) - 1)
    )
    folio_counts.append(round(value, 2))

df = pd.DataFrame({
    "date": dates,
    "folio_count_cr": folio_counts
})

fig = px.line(
    df,
    x="date",
    y="folio_count_cr",
    title="Mutual Fund Folio Growth (2022-2025)"
)

# Start milestone
fig.add_annotation(
    x="2022-01-01",
    y=13.26,
    text="13.26 Cr",
    showarrow=True
)

# End milestone
fig.add_annotation(
    x="2025-12-01",
    y=26.12,
    text="26.12 Cr",
    showarrow=True
)

fig.write_html("reports/folio_growth.html")

fig.show()

print("Folio Growth Chart Saved Successfully!")