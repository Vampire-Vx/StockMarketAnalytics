from dash import html
import dash_bootstrap_components as dbc
from components.colors import PRIMARY_COLOR, BACKGROUND_COLOR
from utils.fig_utils import convert_hex_to_rgba

BACKGROUND_COLOR_RGBA = convert_hex_to_rgba(BACKGROUND_COLOR)
PRIMARY_COLOR_RGBA = convert_hex_to_rgba(PRIMARY_COLOR, opacity=0.5)

def create_footer():
    link_style = {
    'color': PRIMARY_COLOR,
    'font-weight': 'bold',
    'font-size': '16px',
    'text-decoration': 'none'
    }
    footer = html.Footer(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Span([
                            "Author: ",
                            html.A(
                                "Alfredo Muñoz",
                                href="https://github.com/Alfredomg7",
                                target="_blank",
                                style=link_style
                            )
                        ]),
                        className='text-center'
                    ),
                    dbc.Col(
                        html.Span([
                            "Source code: ",
                            html.A(
                                "GitHub Repository",
                                href="https://github.com/Alfredomg7/StockMarketAnalytics",
                                target="_blank",
                                style=link_style
                            )
                        ]),
                        className='text-center'
                    ),
                    dbc.Col(
                        html.Span([
                            "Data source: ",
                            html.A(
                                "yfinance API",
                                href="https://github.com/ranaroussi/yfinance",
                                target="_blank",
                                style=link_style
                            )
                        ]),
                        className='text-center'
                    ),
                ],
                className='justify-content-center',
            )
        ],
        className='py-2',
        style={
            'background-color': f"{BACKGROUND_COLOR_RGBA}",
            'position': 'fixed',
            'bottom': '0',
            'width': '100%',
            'box-shadow': f"0px 0px 8px {PRIMARY_COLOR_RGBA}",
            'z-index': '1000'
        }
    )
    return footer
                    

            
                    