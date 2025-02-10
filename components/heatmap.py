import plotly.express as px
import polars as pl
from utils.fig_utils import style_fig

def create_correlation_heatmap(corr_matrix: pl.DataFrame, title: str) -> px.imshow:
    labels = corr_matrix.columns
    fig = px.imshow(
        corr_matrix,
        x=labels,
        y=labels,
        title=title,
        zmin=-1,
        zmax=1,
        text_auto=True,
        color_continuous_scale='RdYlGn',
        aspect='auto',
    )
    style_fig(fig, title)
    fig.update_yaxes(title=None)
    return fig