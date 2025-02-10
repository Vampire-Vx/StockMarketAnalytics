import polars as pl
import plotly.express as px
from utils.fig_utils import style_fig

def create_bar_chart(
    data: pl.DataFrame,
    x: str,
    y: str,
    title: str,
    color: str = '#fff',
    orientation: str = 'v',
    show_data_labels: bool = False,
) -> px.bar:
    fig = px.bar(
            data, 
            x=x if orientation == 'v' else y,
            y=y if orientation == 'v' else x,
            title=title,
            orientation=orientation,
            color_discrete_sequence=[color]
        )
    fig.update_traces(
        marker=dict(
            line=dict(width=1, color='DarkSlateGrey'),
            opacity=0.9
        ),
        hovertemplate='%{x}<br>%{y}' if orientation == 'v' else '%{y}<br>%{x}'
    )

    # Add data labels to the chart if enabled
    if show_data_labels:
        fig.update_traces(
            text=data[y].to_list(),
            textposition='outside',
            texttemplate='<b>%{text:$,.0f}</b>',
            textfont=dict(color=color, size=14)
        )

    # Adjust numeric axis range to avoid cutting off the data labels
    if show_data_labels:
        if orientation == 'v':
            fig.update_layout(yaxis_range=[0, data[y].max() * 1.2])
        else:
            fig.update_layout(xaxis_range=[0, data[y].max() * 1.2])
    
    style_fig(fig, title, orientation)
    return fig