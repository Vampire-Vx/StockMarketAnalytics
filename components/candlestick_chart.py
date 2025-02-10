import polars as pl
import plotly.graph_objects as go
from utils.fig_utils import style_fig

def create_candlestick_chart(df: pl.DataFrame, title: str) -> go.Figure:
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'],
                increasing_line_color='green',
                decreasing_line_color='red',
                name=title
            )
        ]
    )
    fig.update_layout(
        yaxis=dict(title='Price (USD)', tickformat='$,.2f'),
    )
    style_fig(fig, title)
    return fig