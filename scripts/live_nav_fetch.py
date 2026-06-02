import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

# convert nav to dataFrame
nav_df = pd.DataFrame(data["data"])

# save CSV
nav_df.to_csv(
    "data/raw/live_nav_125497.csv",
    index=False
)

print("CSV Saved Successfully")
print("Rows:", nav_df.shape[0])
print("Columns:", nav_df.shape[1])

print(nav_df.head())