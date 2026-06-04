import requests
import pandas as pd

# Scheme codes provided by mentor
scheme_codes = [
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

all_schemes = []

for code in scheme_codes:

    print(f"Fetching Scheme: {code}")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    meta = data["meta"]

    all_schemes.append(meta)

# Convert to DataFrame
df = pd.DataFrame(all_schemes)

# Save CSV
df.to_csv(
    "data/raw/five_schemes_nav.csv",
    index=False
)

print("\nCSV Saved Successfully")

print("\nShape:")
print(df.shape)

print("\nData:")
print(df)