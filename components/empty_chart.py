import plotly.graph_objects as go
from utils.fig_utils import style_fig

def create_empty_chart(title: str) -> go.Figure:
    fig = go.Figure()
    fig.add_annotation(
        text='No data available for selected filters',
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=18, family='Arial', color='white'),
        xref='paper',
        yref='paper',
    )
    style_fig(fig, title)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    return fig
