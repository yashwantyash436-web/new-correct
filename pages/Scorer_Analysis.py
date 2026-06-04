import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⚽ Goal Scorer Analytics")

df = pd.read_csv("data/goalscorers.csv")

top_scorers = (
    df["scorer"]
    .value_counts()
    .head(20)
    .reset_index()
)

top_scorers.columns = ["Scorer", "Goals"]

fig = px.bar(
    top_scorers,
    x="Goals",
    y="Scorer",
    orientation="h",
    title="Top 20 Goal Scorers"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Top Scorers Table")
st.dataframe(top_scorers)
