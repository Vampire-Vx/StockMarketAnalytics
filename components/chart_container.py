import dash_bootstrap_components as dbc
from dash import dcc, html
from typing import List, Union

def create_chart_container(
    content_id: dict,
    inputs: List[Union[dbc.Row, dbc.Col]] = None,
    bg_color: str = "white",
    loading_color: str = "#119DFF",
    title: str = None,
) -> dbc.Card:
    input_components = inputs or []
    class_name = "mb-4 shadow-sm"
    if bg_color == "dark":
        class_name += " bg-dark text-light"
    elif bg_color:
        class_name += f" bg-{bg_color}"

    # Build card container
    container = dbc.Card(
        dbc.CardBody(
            [
                html.H4(title, className="card-title text-center mb-4") if title else None,
                *input_components,
                html.Hr(className="my-3") if input_components else None,
                # Loading spinner wraps content
                dcc.Loading(
                    type="circle",
                    color=loading_color,
                    children=[dcc.Graph(id=content_id)]
                )
            ]
        ),
        class_name=class_name
    )
    return container