import polars as pl
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils.fig_utils import style_fig

def create_composite_chart(df: pl.DataFrame, indicators: list, dt_breaks:pl.DataFrame) -> go.Figure:
    fig = make_subplots(
        rows=3, cols=1, vertical_spacing=0.005,
        shared_xaxes=True, row_heights=[0.7,0.3, 0.0005]
    )

    fig.add_trace(
        go.Candlestick(
            x=df['date'],
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            increasing_line_color='green',
            decreasing_line_color='red',
        ),
        row=1, col=1
    )
    fig.add_trace(
        go.Candlestick(
            x=df['date'],
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            increasing_line_color='green',
            decreasing_line_color='red',
        ),
        row=2, col=1
    )

    fig.add_trace(
        go.Candlestick(
            x=df['date'],
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            increasing_line_color='green',
            decreasing_line_color='red',
        ),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=df['date'],
            y=df['close'],
            hoverinfo="none"  # Disable hover info
        ),
        row=3, col=1
    )

    for i in range(1,4):
        show_range=False
        if i==3:
            show_range = True
            fig.update_yaxes(
                showticklabels=False,             # Hide y-axis tick labels
                title_text="",                    # Remove y-axis title
                showgrid=False,                   # Hide y-axis grid lines
                zeroline=False,                   # Hide y-axis zero line
                visible=False,                    # Hide y-axis entirely
                row=i, col=1
            )
        fig.update_xaxes(
            rangeslider_visible=show_range,
            rangeslider_thickness=0.1,
            rangebreaks=[dict(values=dt_breaks)],
            row=i, col=1
        )
    fig.update_layout(
        yaxis=dict(title=None, tickformat=',.2f'),
    )
    fig.update_yaxes(autorange=True, fixedrange=False, row=1, col=1)  # First subplot
    fig.update_yaxes(autorange=True, fixedrange=False, row=2, col=1)  # Second subplot
    style_fig(fig, None)
    return fig