from typing import Dict, Union
from io import StringIO
from dash import Dash, Input, Output, State, callback_context
import dash_ag_grid as dag
import pandas as pd
import components as cmp
from services.portfolio import add_stock, edit_stock, delete_stock
from utils.fig_utils import prepare_table_data

def register_callbacks(app: Dash) -> None:
    @app.callback(
        [
            Output({"type": "portfolio-data", "section": "global"}, "data"),
            Output({"type": "alert-feedback", "section": "portfolio-form"}, "is_open"),
            Output({"type": "alert-feedback", "section": "portfolio-form"}, "color"),
            Output({"type": "alert-feedback", "section": "portfolio-form"}, "children"),
        ],
        [
            Input({"type": "button-submit", "section": "portfolio-form"}, "n_clicks"),
            Input({"type": "button-edit", "section": "portfolio-form"}, "n_clicks"),
            Input({"type": "button-delete", "section": "portfolio-form"}, "n_clicks"),
        ],
        [
            State({"type": "input-ticker", "section": "portfolio-form"}, "value"),
            State({"type": "input-shares", "section": "portfolio-form"}, "value"),
            State({"type": "portfolio-data", "section": "global"}, "data"),
            State({"type": "price-data", "section": "global"}, "data"),
        ],
        prevent_initial_call=True,
    )
    def handle_portfolio_update(
        add_clicks: int,
        edit_clicks: int,
        delete_clicks: int,
        ticker: str,
        shares: float,
        portfolio_data: Union[str, None],
        price_data: Dict[str, float],
    ) -> tuple[Dict[str, float], bool, str, str]:
        if portfolio_data:
            portfolio_data = pd.read_json(StringIO(portfolio_data), orient="records")
        else:
            portfolio_data = pd.DataFrame()

        # Default alert properties
        alert_open = True
        alert_color = "info"
        alert_message = "No action performed."
        
        # Prevent triggering add_stock on page load
        if add_clicks is None:
            return portfolio_data.to_json(orient="records"), False,alert_color, alert_message
        
        # Identify which button was clicked to trigger the callback
        triggered_id = callback_context.triggered[0]["prop_id"]

        try:
            if "button-submit" in triggered_id:
                if not ticker or shares <= 0:
                    alert_color = "warning"
                    alert_message = "Invalid input. Please enter a valid ticker and positive shares."
                else:
                    price = price_data[ticker]
                    portfolio_data = add_stock(portfolio_data, ticker, shares, price)
                    alert_color = "success"
                    alert_message = f"Added {shares} shares of {ticker}."
            elif "button-edit" in triggered_id:
                if not ticker or ticker not in portfolio_data["Ticker"].values or shares <= 0:
                    alert_color = "warning"
                    alert_message = f"Cannot edit: {ticker} is not in the portfolio or shares are invalid."
                else:
                    portfolio_data = edit_stock(portfolio_data, ticker, shares, price_data[ticker])
                    alert_color = "success"
                    alert_message = f"Updated {ticker} to {shares} shares."
            elif "button-delete" in triggered_id:
                if not ticker or ticker not in portfolio_data["Ticker"].values:
                    alert_color = "warning"
                    alert_message = f"Cannot delete: {ticker} is not in the portfolio."
                else:
                    portfolio_data = delete_stock(portfolio_data, ticker)
                    alert_color = "danger"
                    alert_message = f"Deleted {ticker} from the portfolio."
        except Exception as e:
            alert_color = "danger"
            alert_message = f"Error: {str(e)}"
        portfolio_data_json = portfolio_data.to_json(orient="records")
        return portfolio_data_json, alert_open, alert_color, alert_message

    # Callback to display the portfolio list
    @app.callback(
        Output({"type": "output-portfolio-data", "section": "portfolio-form"}, "children"),
        Input({"type": "portfolio-data", "section": "global"}, "data"),
        prevent_initial_call=True,
    )
    def update_portfolio_list(portfolio_data: pd.DataFrame) -> dag.AgGrid:
        # Prepare the portfolio data for display
        portfolio_df = pd.read_json(StringIO(portfolio_data), orient="records")
        if not portfolio_df.empty:
            table_data = prepare_table_data(portfolio_df)
        else:    
            table_data = []

        # Define Ag-Grid column definitions
        column_defs = [
            {"headerName": "Ticker", "field": "Ticker", "sortable": True, "filter": True},
            {"headerName": "Shares", "field": "Shares", "sortable": True, "filter": True, "type": "numericColumn"},
            {"headerName": "Price ($)", "field": "Price", "sortable": True, "filter": True},
            {"headerName": "Value ($)", "field": "Value", "sortable": True, "filter": True},
            {"headerName": "Weight (%)", "field": "Weight", "sortable": True, "filter": True},
        ]

        # Create and return the Ag-Grid table
        return cmp.create_table(
            id={"type": "portfolio-table", "section": "portfolio-form"},
            columns=column_defs,
            data=table_data,
        )