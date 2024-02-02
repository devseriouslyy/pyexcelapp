import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Ageing Dashboard", page_icon=":bar_chart:", layout="wide")


df = pd.read_excel(
        io="AgeingTickets.xlsx",
        engine="openpyxl",
        sheet_name="Aging Master Sheet",
        skiprows=0,
        usecols="B:Q",
        nrows=2010,
    )

st.dataframe(df)

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
tower = st.sidebar.multiselect(
    "Select the tower:",
    options=df["Tower"].unique(),
    default=df["Tower"].unique()
)

priority = st.sidebar.multiselect(
    "Select the priority type:",
    options=df["Priority"].unique(),
    default=df["Priority"].unique(),
)

age = st.sidebar.multiselect(
    "Select the age:",
    options=df["Aging_Window"].unique(),
    default=df["Aging_Window"].unique()
)

df_selection = df.query(
    "Tower == @tower and Priority == @priority and Aging_Window == @age"
)

st.dataframe(df_selection)
