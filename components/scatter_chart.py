import plotly.express as px
import polars as pl
from utils.fig_utils import style_fig

def create_scatter_chart(df: pl.DataFrame, x: str, y: str, title: str, color: str) -> px.scatter:
    fig = px.scatter(df, x=x, y=y, title=title)
    fig.update_traces(
        marker=dict(size=8, 
                    color=color,
                    symbol='diamond',
                    opacity=0.9,
                ),
        hovertemplate='%{x}<br>%{y}'
    )
    style_fig(fig, title)
    return fig