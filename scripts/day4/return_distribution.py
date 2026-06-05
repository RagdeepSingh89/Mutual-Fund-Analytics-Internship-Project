import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/daily_returns.csv"
)

df["daily_return"].hist(
    bins=50
)

plt.title("Daily Return Distribution")
plt.xlabel("Return")
plt.ylabel("Frequency")

plt.show()