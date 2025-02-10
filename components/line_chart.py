import polars as pl
import plotly.express as px
from utils.fig_utils import style_fig

def create_line_chart(data: pl.DataFrame, x: str, y: str, title: str, color: str) -> px.line:
    fig = px.line(data, x=x, y=y, title=title, color_discrete_sequence=[color])
    fig.update_yaxes(tickprefix='$', title='Price (USD)')
    fig.update_traces(
        line=dict(width=2),
        hovertemplate='%{x}<br>%{y:$,.2f}'
    )
    style_fig(fig, title)
    return fig