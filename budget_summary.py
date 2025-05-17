def analyze_budget(df):
    df_clean = df.dropna(subset=["Category", "Amount"])
    df_clean["Amount"] = df_clean["Amount"].astype(float)
    summary = df_clean.groupby("Category")["Amount"].sum()
    net_savings = df_clean["Amount"].sum() * 0.1  # Example: 10% saved
    return summary, net_savings
