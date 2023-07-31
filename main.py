import pandas as pd
import streamlit as st
import numpy as np

import app




def main():

    data = app.get_bluecoins_data()
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d %H:%M:%S')
    
    st.subheader("All the data")
    if st.checkbox('Show dataframe', key='all_data'):
        st.table(data)

    st.subheader('Transactions per month')
    if st.checkbox('Show dataframe', key='transactions_per_month'):
        year_filter = st.slider('year', 2021, 2023) 
        filtered_data = data[(data['Date'] > f"{year_filter}-01-01") & (data['Date'] < f"{year_filter}-12-31")]

        m = filtered_data['Date'].dt.month
        new = data.groupby([m]).size()

        st.bar_chart(new)


if __name__ == "__main__":
    main()
