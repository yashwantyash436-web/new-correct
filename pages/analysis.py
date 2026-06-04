import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Country Analysis")

df = pd.read_csv("data/results.csv")

teams = sorted(
    list(
        set(df["home_team"]).union(
            set(df["away_team"])
        )
    )
)

team = st.selectbox(
    "Select Team",
    teams
)

home_matches = df[df["home_team"] == team]
away_matches = df[df["away_team"] == team]

wins = draws = losses = 0

for _, row in home_matches.iterrows():

    if row["home_score"] > row["away_score"]:
        wins += 1

    elif row["home_score"] < row["away_score"]:
        losses += 1

    else:
        draws += 1

for _, row in away_matches.iterrows():

    if row["away_score"] > row["home_score"]:
        wins += 1

    elif row["away_score"] < row["home_score"]:
        losses += 1

    else:
        draws += 1

matches = wins + draws + losses

c1, c2, c3, c4 = st.columns(4)

c1.metric("Matches", matches)
c2.metric("Wins", wins)
c3.metric("Draws", draws)
c4.metric("Losses", losses)

chart_data = pd.DataFrame({
    "Result": ["Wins", "Draws", "Losses"],
    "Count": [wins, draws, losses]
})

fig = px.pie(
    chart_data,
    values="Count",
    names="Result",
    title=f"{team} Performance"
)

st.plotly_chart(fig, use_container_width=True)
