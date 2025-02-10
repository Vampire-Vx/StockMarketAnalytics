import dash_bootstrap_components as dbc

def create_label(text: str, html_for: str) -> dbc.Label:
    label = dbc.Label(
                text, 
                html_for=html_for,
                style={'font-size': '16px', 'font-weight': '500'}
        )
    return label