# guide/layout.py
from dash import html
import dash_bootstrap_components as dbc

def create_layout() -> dbc.Container:
    # Header
    header = html.H1("User Guide", className="text-center display-4 text-light")
    description = html.P(
        "Learn how to navigate and make the most out of the Stock Market Analytics App.",
        className="text-center opacity-75 fs-4"
    )

    # Navigation Buttons
    navigation_buttons_group = dbc.Card(
        dbc.CardBody(
            dbc.ButtonGroup(
                [
                    dbc.Button("Market Dashboard", href="/", color="success"),
                    dbc.Button("My Portfolio", href="/portfolio-form", color="info"),
                    dbc.Button("Portfolio Dashboard", href="/portfolio-dashboard", color="secondary"),
                ],
                size="sm",
                className="w-100",
                style={"justify-content": "center"}
            )
        ),
        class_name="mb-4 shadow-sm bg-dark text-light"
    )

    # Glossary Card
    glossary_card = dbc.Card(
        dbc.CardBody([
            html.H4("Glossary of Terms", className="card-title"),
            html.Ul([
                html.Li([
                    html.Strong("Ticker:"), 
                    " The unique symbol representing a stock. For example, AAPL for Apple Inc."
                ]),
                html.Li([
                    html.Strong("Shares:"), 
                    " The number of units of a stock you own."
                ]),
                html.Li([
                    html.Strong("Price:"), 
                    " The current market price of a stock."
                ]),
                html.Li([
                    html.Strong("Value:"), 
                    " The total value of your holding (Shares × Price)."
                ]),
                html.Li([
                    html.Strong("HHI:"), 
                    " The Herfindahl–Hirschman Index—a measure of portfolio concentration."
                ]),
                # Add more glossary items as needed.
            ])
        ]),
        className="mb-4 shadow-sm bg-dark text-light"
    )

    # Data Source Information Card
    data_source_card = dbc.Card(
        dbc.CardBody([
            html.H4("Data Source Information", className="card-title"),
            html.P("Data is fetched from Yahoo Finance using the yfinance API and stored in an SQLite database. Data is updated daily."),
        ]),
        className="mb-4 shadow-sm bg-dark text-light"
    )

    # Dashboard Sections Overview Card
    sections_card = dbc.Card(
        dbc.CardBody([
            html.H4("Dashboard Sections Overview", className="card-title"),
            html.Ul([
                html.Li([
                    html.Strong("Market Dashboard:"), 
                    " Explore general stock market insights through various charts and filters."
                ]),
                html.Li([
                    html.Strong("My Portfolio:"), 
                    " Create or modify your custom portfolio by adding, editing, or deleting stocks."
                ]),
                html.Li([
                    html.Strong("Portfolio Dashboard:"), 
                    " View key performance indicators (KPIs) and data insights about your portfolio"
                ]),
            ]),
            html.P("Use the sidebar navigation to switch between these sections.")
        ]),
        className="mb-4 shadow-sm bg-dark text-light"
    )

    # Assemble the layout
    layout = dbc.Container([
        dbc.Row(dbc.Col(header, width=12), className="mt-4 mb-2"),
        dbc.Row(dbc.Col(description, width=12), className="mb-4"),
        html.Hr(className="mb-4"),
        dbc.Row(
            dbc.Col(navigation_buttons_group, xl=6, lg=8, md=10, sm=12),
            className="mb-4 justify-content-center"
        ),
        dbc.Row(
            dbc.Col(glossary_card, md=12, lg=10, xl=8),
            className="mb-4 justify-content-center"
        ),
        dbc.Row(
            dbc.Col(data_source_card, md=12, lg=10, xl=8),
            className="mb-4 justify-content-center"
        ),
        dbc.Row(
            dbc.Col(sections_card, md=12, lg=10, xl=8),
            className="mb-4 justify-content-center"
        )
    ], fluid=True)

    return layout
