def total_goals(df):
    return df["home_score"].sum() + df["away_score"].sum()

def total_matches(df):
    return len(df)

def total_tournaments(df):
    return df["tournament"].nunique()
