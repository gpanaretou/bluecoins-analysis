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

    year_filter = st.slider('Year to view data about', 2021, 2023)

    st.subheader('Transactions per month')
    if st.checkbox('Show Graph', key='transactions_per_month'):
         
        filtered_data = data[(data['Date'] > f"{year_filter}-01-01") & (data['Date'] < f"{year_filter}-12-31")]

        m = filtered_data['Date'].dt.month
        new = data.groupby([m]).size()
        st.bar_chart(new)

    st.subheader('Total Expenses per month')
    if st.checkbox('Show Data', key='transactions per month'):
        filtered_data = data[(data['Date'] > f"{year_filter}-01-01") & (data['Date'] < f"{year_filter}-12-31")]
        
        c = filtered_data[filtered_data['Type'] == 'Expense']

        m = c['Date'].dt.strftime('%B')

        new = data.groupby([m], sort=False)['Amount'].sum()
        avg = new.iloc[::].sum()/len(new)
        df = pd.DataFrame(new)
        df.loc[f'Average for {year_filter}'] = avg

        st.table(df)
        pass



if __name__ == "__main__":
    main()
