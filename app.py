import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Ticketing Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
df = pd.read_excel(
        io="Ticket-Ageing-test.xlsx",
        engine="openpyxl",
        sheet_name="IM",
        skiprows=1,
        usecols="A:G",
        nrows=105,
)
    
# Display the dataframe
st.dataframe(df)

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")

state = st.sidebar.multiselect(
    "Select state:",
    options=df["State"].unique(),
    default=df["State"].unique()
)

account = st.sidebar.multiselect(
    "Select Account:",
    options=df["Account"].unique(),
    default=df["Account"].unique()
)

aging = st.sidebar.multiselect(
    "Select Aging:",
    options=df["Age"].unique(),
    default=df["Age"].unique()
)

df_selection = df.query(
    "State == @state & Account == @account & Age == @aging" 
)




st.dataframe(df_selection)



