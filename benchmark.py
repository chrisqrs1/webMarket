import streamlit as st
import plotly.graph_objects as go
from utils import load_data, pathData

benchmarkIndices = load_data(pathData, 'benchmarks.parquet.gzip').drop('spread', axis=1)
benchmarkBreakEvens = load_data(pathData, 'benchmarkBreakEvens.parquet.gzip')

def benchmark():
    st.subheader("Benchmark")
    st.write("Benchmark: comparison of implied convexity with VVIX Index")

    st.header("Benchmark Implied Convexity vs VVIX")
    fig = go.Figure()
    colors = ['red', 'blue']
    for c, (strategy, values) in enumerate(benchmarkIndices.items()):
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
        title_text='investible Strategies',
        title_x = 0.5,
        xaxis=dict(title='date'),
        yaxis=dict(title='value'),
        legend=dict(yanchor='top', y=1.1, xanchor='center', x=0.5, orientation='h',
                    borderwidth=1, bordercolor='white', font=dict(size=12)),
    )

    st.plotly_chart(fig, use_container_width=True)


    st.header("Theoretical Break Evens on Benchmark")
    fig = go.Figure()
    colors = ['red', 'blue', 'orange', 'green']
    for c, (strategy, values) in enumerate(benchmarkBreakEvens.items()):
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
        title_text='Theoretical Break Evens on Benchmark',
        title_x = 0.5,
        xaxis=dict(title='date'),
        yaxis=dict(title='value'),
        legend=dict(yanchor='top', y=1.1, xanchor='center', x=0.5, orientation='h',
                    borderwidth=1, bordercolor='white', font=dict(size=12)),
    )
    st.plotly_chart(fig, use_container_width=True)

