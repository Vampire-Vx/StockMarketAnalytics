from dash import html
import dash_bootstrap_components as dbc
import components as cmp

def create_layout() -> dbc.Container:
    title = html.H1("Portfolio Dashboard", className="text-center display-4 text-light")
    description = html.P("Analyze insights about your custom portfolio", className="text-center opacity-75 fs-4")

    # Navigation Buttons
    navigation_buttons_group = dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    dbc.ButtonGroup(
                        [
                            dbc.Button("My Portfolio", href="/portfolio-form", color="success"),
                            dbc.Button("Market Dashboard", href="/", color="info"),
                            dbc.Button("Guide", href="/guide", color="secondary"),
                        ],
                        size="sm",
                        className="w-100",
                        style={"justify-content": "center"}
                    )
                ),
                class_name="mb-4 shadow-sm bg-dark text-light"
            ),
            xl=6, lg=8, md=10, sm=12
        )
    ], class_name="mb-4 justify-content-center")

    # KPI Cards
    kpi_cards_group = dbc.Row([
        dbc.Col(cmp.create_kpi_card("Total Value", "-", color="success", value_id={'type': 'kpi-value', 'section': 'Total Value'}), xl=3, md=6, xs=12, class_name="mb-4"),
        dbc.Col(cmp.create_kpi_card("Unique Stocks", "-", color="info", value_id={'type': 'kpi-value', 'section': 'Unique Stocks'}), xl=3, md=6, xs=12, class_name="mb-4"),
        dbc.Col(cmp.create_kpi_card("AVG Price", "-", color="warning", value_id={'type': 'kpi-value', 'section': 'AVG Price'}), xl=3, md=6, xs=12, class_name="mb-4"),
        dbc.Col(cmp.create_kpi_card("HHI", "-", color="primary", value_id={'type': 'kpi-value', 'section': 'HHI'}), xl=3, md=6, xs=12, class_name="mb-4"),
    ], class_name="mb-4 justify-content-center")

    # Chart Containers
    portfolio_distribution_chart =  cmp.create_chart_container(
        content_id={'type': 'portfolio-distribution-chart', 'section': 'portfolio'},
        bg_color='dark',
        loading_color=cmp.PRIMARY_COLOR,
    )

    sector_distribution_chart= cmp.create_chart_container(
        content_id={'type': 'sector-distribution-chart', 'section': 'portfolio'},
        bg_color='dark',
        loading_color=cmp.PRIMARY_COLOR
    )

    # Layout
    layout = dbc.Container([
        dbc.Row([dbc.Col(title, width=12)], class_name="my-2 text-center"),
        dbc.Row([dbc.Col(description, width=12)], class_name="mb-4 text-center"),
        html.Hr(className='mb-4'),
        navigation_buttons_group,
        kpi_cards_group,
        dbc.Row([
            dbc.Col(portfolio_distribution_chart, xl=6, md=12, sm=12),
            dbc.Col(sector_distribution_chart, xl=6, md=12, sm=12)
        ], class_name="mb-4"),
    ], fluid=True)

    return layout
