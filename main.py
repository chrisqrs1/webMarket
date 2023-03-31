# App URL : chrisqrs1-webmarket-main-sa7j34 .streamlit.app -> qrs1-implied-convexity-vix.streamlit.app 
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from PIL import Image
from utils import set_logger

logger = set_logger(
    log_directory='/log',
    log_file='streamlit.log',
    name='streamlit'
)

st.set_page_config(
    page_title="all about VIX",
    page_icon=":guardsman:",  # "🧊",
    layout="wide",  # "centered"
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

from benchmark import benchmark
from investible_strategies import investible_strategies
# from simple_option_pnl_risks import simple_option_pnl_risks

def select_page():
    # Create sidebar with page options
    menu = [
        "Home",
        "Benchmark",
        "Investible Strategies (systemtic short vol)",
        "Simple Option Strategy",
        "Investible Strategies (short vol AI)"
        "VIX options market", "VIX roll down", "VIX Beta to Market",
        'systematic options strategies',
        'CFTC traders commitments reports',
        'VIX related ETNs & ETFs',
        'VIX Beta and Correlation',
        'historical distributions'
    ]
    page = st.sidebar.selectbox("Select a page", menu)

    if page == "Home":
        st.subheader("Home Page")
        st.write("Welcome to my navigation app!")
        logo = Image.open('images/Logo_QRS1_VERT.jpg')
        st.image(logo, caption='Logo of your company', use_column_width=True)
    elif page == "Benchmark":
        logger.info(f'click on page {page}')
        benchmark()
    elif page == "Investible Strategies (systemtic short vol)":
        logger.info(f'click on page {page}')
        investible_strategies()
    else:
        logger.info(f'click on page {page}')
        st.write('not ready yet')

def main():
    select_page()

if __name__ == "__main__":



    main()






#
# col1, col2 = st.columns([3, 2])
#
# with col1:
#     st.header("Benchmark Implied Convexity vs VVIX")
#
#     fig = go.Figure()
#     colors = ['red', 'blue']
#     for c, (strategy, values) in enumerate(benchmarkIndices.items()):
#         fig.add_scatter(
#             x=values.index,
#             y=values,
#             name=strategy,
#             mode='lines',
#             line={
#                 'color': colors[c % len(colors)],
#                 'width': 4
#             },
#         )
#     layout = go.Layout(
#         title='investible Strategies',
#         xaxis=dict(title='date'),
#         yaxis=dict(title='value'),
#     )
#     st.plotly_chart(fig, use_container_width=True)
#
#
#     st.header("investible Strategies")
#     fig = go.Figure()
#     colors = ['red', 'blue']
#     for c, (strategy, values) in enumerate(investibleIndices.items()):
#         fig.add_scatter(
#             x=values.index,
#             y=values,
#             name=strategy,
#             mode='lines',
#             line={
#                 'color': colors[c % len(colors)],
#                 'width': 4
#             },
#         )
#     layout = go.Layout(
#         title='investible Strategies',
#         xaxis=dict(title='date'),
#         yaxis=dict(title='value'),
#     )
#     st.plotly_chart(fig, use_container_width=True)
#
#
#     st.header("Theoretical Break Evens on Benchmark")
#     fig = go.Figure()
#     colors = ['red', 'blue', 'orange', 'green']
#     for c, (strategy, values) in enumerate(benchmarkBreakEvens.items()):
#         fig.add_scatter(
#             x=values.index,
#             y=values,
#             name=strategy,
#             mode='lines',
#             line={
#                 'color': colors[c % len(colors)],
#                 'width': 4
#             },
#         )
#     layout = go.Layout(
#         title='investible Strategies',
#         xaxis=dict(title='date'),
#         yaxis=dict(title='value'),
#     )
#     st.plotly_chart(fig, use_container_width=True)
#
#
# with col2:
#
#     for strategy, tbl in tables.items():
#         st.write(strategy)
#         st.dataframe(tbl)
#
#     st.header("Distribution of break even range")
#     st.dataframe(benchmarkBreakEvens.describe(percentiles=[0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]).drop(['count', 'std']).round(2))
#
#
