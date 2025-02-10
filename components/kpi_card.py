from dash import html
import dash_bootstrap_components as dbc

def create_kpi_card(kpi_name: str, kpi_value: str, color: str = "white", value_id=None) -> dbc.Card:
    class_name = "mb-4 shadow-sm"
    if color == "dark":
        class_name += " bg-dark text-light"
    elif color:
        class_name += f" bg-{color}"
    
    kpi_card = dbc.Card(
                dbc.CardBody(
                    [
                        html.H4(kpi_name, className="card-title"),
                        html.H2(kpi_value, className="card-text", id=value_id)
                    ]
                )
            )
    return kpi_card