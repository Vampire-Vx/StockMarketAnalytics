from dash import html
import dash_bootstrap_components as dbc

def create_sidebar(paths: dict) -> dbc.Col:
    sidebar =  dbc.Col(
        [
            html.H2(
                    "MENU",
                    className="text-light",
                    style={
                        'font-size': '8px + 2vw',
                        'font-weight': '200',
                        'width': '100%',
                    }),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink(path, href=paths[path], className='text-light')) for path in paths
                ],
                vertical=True,
                pills=True,
            ),
        ],
        width=2,
        className="bg-dark border-right d-none d-md-block",
        style={
            "position": "fixed",
            "top": 0,
            "left": 0,
            "bottom": 0,
            "height": "100%",
            "padding": "2rem 1rem",
        },
    )
    return sidebar