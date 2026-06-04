import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏆 Tournament Analytics")

df = pd.read_csv("data/results.csv")

tournament = st.selectbox(
    "Select Tournament",
    sorted(df["tournament"].unique())
)

filtered = df[
    df["tournament"] == tournament
]

matches = len(filtered)

goals = (
    filtered["home_score"].sum()
    +
    filtered["away_score"].sum()
)

c1, c2 = st.columns(2)

c1.metric(
    "Matches",
    matches
)

c2.metric(
    "Goals",
    goals
)

top_teams = (
    filtered["home_team"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_teams.columns = [
    "Team",
    "Matches"
]

fig = px.bar(
    top_teams,
    x="Team",
    y="Matches",
    title=f"Top Teams in {tournament}"
)

st.plotly_chart(fig, use_container_width=True)
