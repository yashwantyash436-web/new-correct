import pandas as pd

def load_results():
    return pd.read_csv("data/results.csv")

def load_scorers():
    return pd.read_csv("data/goalscorers.csv")

def load_shootouts():
    return pd.read_csv("data/shootouts.csv")

def load_former_names():
    return pd.read_csv("data/former_names.csv")
