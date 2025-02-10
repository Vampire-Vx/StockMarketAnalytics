from typing import Dict, Union, List
import plotly.graph_objects as go
import pandas as pd

def style_fig(fig: go.Figure, title: str, orientation: str = 'v') -> go.Figure:
    """Style the figure with a dark theme and custom layout."""
    xaxis_title = None if orientation == "v" else "Values"
    yaxis_title = None if orientation == "h" else "Values"
    
    fig.update_layout(
        template='plotly_dark',
        title=dict(
            text=title,
            font=dict(size=24, family='Arial', color='white'),
            x=0.5,
        ),
        xaxis=dict(
            title=xaxis_title,
            showgrid=orientation == 'h',
            zeroline=False,
            title_font=dict(size=20, family='Arial', color='white')
        ),
        yaxis=dict(
            title=yaxis_title,
            showgrid=orientation == 'v',
            zeroline=False,
            title_font=dict(size=20, family='Arial', color='white')
        ),
        margin=dict(l=40, r=40, t=50, b=30),
    )
    return fig

def format_currency(value: float) -> str:
    """Format a numeric value as a currency string."""
    return f"${value:,.2f}"

def format_percent(value: float) -> str:
    """Format a numeric value as a percentage string."""
    return f"{value:.2%}"

def prepare_table_data(df: pd.DataFrame) -> List[Dict[str, Union[str, float]]]:
    """Prepare the DataFrame for display in a Ag-Grid Table."""
    formatted_data = df.copy()
    formatted_data["Price"] = formatted_data["Price"].apply(format_currency)
    formatted_data["Value"] = formatted_data["Value"].apply(format_currency)
    formatted_data["Weight"] = formatted_data["Weight"].apply(format_percent)
    table_data = formatted_data.to_dict("records")
    return table_data

def convert_hex_to_rgba(hex_color, opacity=1.0):
    hex_color = hex_color.lstrip('#')
    rgb_tuple = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"rgba({rgb_tuple[0]}, {rgb_tuple[1]}, {rgb_tuple[2]}, {opacity})"