import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Football Overview Dashboard")

df = pd.read_csv("data/results.csv")

total_matches = len(df)
total_goals = df["home_score"].sum() + df["away_score"].sum()
total_teams = len(set(df["home_team"]).union(set(df["away_team"])))
total_tournaments = df["tournament"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Matches", f"{total_matches:,}")
col2.metric("Goals", f"{total_goals:,}")
col3.metric("Teams", total_teams)
col4.metric("Tournaments", total_tournaments)

st.divider()

st.subheader("Top 10 Tournaments")

top_tournaments = (
    df["tournament"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_tournaments.columns = ["Tournament", "Matches"]

fig = px.bar(
    top_tournaments,
    x="Tournament",
    y="Matches",
    title="Most Played Tournaments"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Goals Distribution")

goal_df = pd.DataFrame({
    "Type": ["Home Goals", "Away Goals"],
    "Goals": [
        df["home_score"].sum(),
        df["away_score"].sum()
    ]
})

fig2 = px.pie(
    goal_df,
    values="Goals",
    names="Type"
)

st.plotly_chart(fig2, use_container_width=True)
