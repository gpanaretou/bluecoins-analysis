import streamlit as st
import pandas as pd

@st.cache_data
def get_bluecoins_data():
    path = 'app/data/transactions_list_30-7-23.csv'
    df = pd.read_csv(path)
    return df

