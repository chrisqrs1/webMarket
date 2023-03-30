import streamlit as st
import plotly.graph_objects as go
from pathlib import Path
import pandas as pd

from utils import load_data, pathProcessedData

option_decomposition = load_data(pathProcessedData, 'option_decomposition.parquet.gzip')
greeks = load_data(pathProcessedData, 'greeks.parquet.gzip')

expiration_dates = option_decomposition.index.get_level_values('expiration_date').unique().sort_values()
expiration_dates_codes = [expiration_date.strftime('%b-%y') for expiration_date in expiration_dates]

def simple_option_pnl_risks():
    # User input area
    st.header("Option Information")
    strike = st.number_input("Enter the strike:", value=20.0)
    call_put = st.selectbox("Select option type:", options=["call", "put"], index=0)
    expiration_date_code = st.selectbox("Select expiration date:", options=expiration_dates_codes, index=len(expiration_dates)-1)
    quantity = st.number_input("Enter quantity of option:", value=1)
    delta_hedge = st.checkbox("Delta hedge on close", help='theoretical B&S delta hedge on close based on level of implied forward')

    expiration_date = expiration_dates[expiration_dates_codes.index(expiration_date_code)]
    decomp = option_decomposition.xs(expiration_date, level='expiration_date').xs(call_put[0].upper(), level='call_put').xs(strike, level='strike')
    decomp = decomp.droplevel(['stock_id', 'root_id', 'expiration_id', 'root_symbol', 'time', 'style', 'ticker', 'instrumentName'])
    decomp = decomp.loc[:, decomp.columns.str.startswith('PnL')]
    decomp = decomp.dropna(axis=1, how='all').dropna(axis=0, how='any')
    if delta_hedge:
        decomp.drop(['PnL_delta', 'PnL_total'], axis=1, inplace=True)
    else:
        decomp.drop(['PnL_total_delta_hedged'], axis=1, inplace=True)


    # Display chart and table
    st.header("Chart")
    st.line_chart(decomp.cumsum(0))

    st.header("Table")
    st.dataframe(decomp.sum(0).to_frame().T)
