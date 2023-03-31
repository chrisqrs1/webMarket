import streamlit as st
import plotly.graph_objects as go
from utils import load_data, pathData

investibleStrategies = load_data(pathData, 'investibleStrategies.parquet.gzip')
performance_tables = {strategy: load_data(pathData, f'performance_table_{strategy}.parquet.gzip') for strategy in investibleStrategies.columns}

def investible_strategies():
    st.subheader("investible strategies_page")
    st.write("based on concept of implied convexity: two versions : sell and hold monthly or daily rolled")

    st.header("investible Strategies")
    fig = go.Figure()
    colors = ['red', 'blue', 'green']
    for c, (strategy, values) in enumerate(investibleStrategies.items()):
        fig.add_scatter(
            x=values.index,
            y=values,
            name=strategy,
            mode='lines',
            line={
                'color': colors[c % len(colors)],
                'width': 4
            },
        )
    fig.update_layout(
        title='investible Strategies',
        xaxis=dict(title='date'),
        yaxis=dict(title='value'),
    )
    st.plotly_chart(fig, use_container_width=True)

    for strategy, performance_table in performance_tables.items():
        st.header(strategy)
        performance_table['Total'] = performance_table.sum(1)
        st.dataframe(performance_table.style.background_gradient(axis=None, cmap="RdYlGn").format(precision=2))

        fig = go.Figure()
        fig.add_histogram(x=performance_table.drop('Total', axis=1).values.flatten()
        )
        st.plotly_chart(fig, use_container_width=True)
