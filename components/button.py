import dash_bootstrap_components as dbc

def create_button(id: str, text: str, color: str) -> dbc.Button:
    button = dbc.Button(
                text,
                id=id,
                color=color,
                style={'width': '100%'}
        )
    return button