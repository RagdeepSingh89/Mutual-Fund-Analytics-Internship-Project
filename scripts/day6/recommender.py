import pandas as pd

sharpe_df = pd.read_csv('data/processed/sharpe_ratio.csv')

risk_map = {
    'Low':      ['Low'],
    'Moderate': ['Moderate'],
    'High':     ['High', 'Very High']
}

def recommend_funds(risk_level, top_n=3):
    risk_level = risk_level.strip().title()
    if risk_level not in risk_map:
        print("Invalid input. Use Low / Moderate / High")
        return
    categories = risk_map[risk_level]
    filtered = sharpe_df[sharpe_df['risk_category'].isin(categories)]
    top = filtered.nlargest(top_n, 'sharpe_ratio')[['scheme_name', 'risk_category', 'sharpe_ratio']]
    print(f"\nTop {top_n} funds — {risk_level} risk:")
    print(top.to_string(index=False))
    return top

if __name__ == '__main__':
    risk = input("Enter risk level (Low/Moderate/High): ").strip()
    recommend_funds(risk)
