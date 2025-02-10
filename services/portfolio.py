import pandas as pd
import numpy as np

def add_stock(portfolio: pd.DataFrame, ticker: str, shares: float, current_price: float) -> pd.DataFrame:
    """Add or update shares for a stock in the portfolio."""
    try:
        validate_inputs(ticker, shares, portfolio)
        if not portfolio.empty and ticker in portfolio["Ticker"].values:
            current_shares = portfolio.loc[portfolio["Ticker"] == ticker, "Shares"].values[0]
            portfolio = edit_stock(portfolio, ticker, current_shares + shares, current_price)
        else:
            new_stock = {
                "Ticker": ticker,
                "Shares": round(shares, 2),
                "Price": round(current_price, 2),
                "Value": round(shares * current_price, 2),
                "Weight": 0
            }
            portfolio = pd.concat([portfolio, pd.DataFrame([new_stock])], ignore_index=True)
            portfolio = calculate_weights(portfolio)
    except Exception as e:
        print(f"Error during add_stock: {e}")
    return portfolio

def edit_stock(portfolio: pd.DataFrame, ticker: str, shares: float, current_price: float) -> pd.DataFrame:
    """Edit the number of shares for a stock in the portfolio."""
    try:
        validate_inputs(ticker, shares, portfolio)
        
        if ticker in portfolio["Ticker"].values:
            portfolio = update_stock_values(portfolio, ticker, shares, current_price)
            portfolio = calculate_weights(portfolio)
        else:
            print(f"Cannot edit: {ticker} is not in the portfolio.")
    except Exception as e:
        print(f"Error during edit_stock: {e}")
    return portfolio

def delete_stock(portfolio: pd.DataFrame, ticker: str) -> pd.DataFrame:
    """Delete a stock from the portfolio."""
    try:
        if not isinstance(ticker, str):
            raise ValueError("Ticker must be a string.")
        if not isinstance(portfolio, pd.DataFrame):
            raise ValueError("Portfolio must be a pandas DataFrame.")
        
        portfolio = portfolio[portfolio["Ticker"] != ticker].reset_index(drop=True)
        portfolio = calculate_weights(portfolio)
    except Exception as e:
        print(f"Error during delete_stock: {e}")
    return portfolio

def calculate_weights(portfolio: pd.DataFrame) -> pd.DataFrame:
    """Recalculate the weights of all stocks in the portfolio."""
    try:
        # Calculate total portfolio value
        total_value = portfolio["Value"].sum()
        # Calculate weight for each stock
        portfolio["Weight"] = round(portfolio["Value"] / total_value, 2) if total_value > 0 else 0
    except Exception as e:
        print(f"Error during calculate_weights: {e}")
    return portfolio

def update_stock_values(portfolio: pd.DataFrame, ticker: str, shares: float, price: float) -> pd.DataFrame:
    """Update the stock's values in the portfolio."""
    portfolio.loc[portfolio["Ticker"] == ticker, "Shares"] = shares
    portfolio.loc[portfolio["Ticker"] == ticker, "Value"] = shares * price
    return portfolio

def validate_inputs(ticker: str, shares: float, portfolio: pd.DataFrame):
    """Validate inputs for portfolio operations."""
    if not isinstance(ticker, str):
        raise ValueError("Ticker must be a string.")
    if not isinstance(shares, (int, float, np.int64, np.float64)) or shares <= 0:
        raise ValueError("Shares must be a positive number.")
    if not isinstance(portfolio, pd.DataFrame):
        raise ValueError("Portfolio must be a pandas DataFrame.")
            
