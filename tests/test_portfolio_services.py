import pytest
import pandas as pd
from services.portfolio import add_stock, edit_stock, delete_stock, calculate_weights

@pytest.fixture
def sample_portfolio():
    """Fixture to create a sample portfolio DataFrame."""
    return pd.DataFrame([
        {"Ticker": "AAPL", "Shares": 10, "Price": 150.0, "Value": 1500.0, "Weight": 0.6},
        {"Ticker": "MSFT", "Shares": 5, "Price": 200.0, "Value": 1000.0, "Weight": 0.4},
    ])

def test_add_stock_new(sample_portfolio):
    """Test adding a new stock to the portfolio."""
    updated_portfolio = add_stock(
        portfolio=sample_portfolio,
        ticker="GOOG",
        shares=2,
        current_price=2800.0
    )
    assert "GOOG" in updated_portfolio["Ticker"].values
    goog_row = updated_portfolio.loc[updated_portfolio["Ticker"] == "GOOG"]
    assert goog_row["Shares"].iloc[0] == 2
    assert goog_row["Value"].iloc[0] == 5600.0
    assert updated_portfolio["Weight"].sum() == pytest.approx(1.0, rel=1e-3)

def test_add_stock_existing(sample_portfolio):
    """Test adding shares to an existing stock."""
    updated_portfolio = add_stock(
        portfolio=sample_portfolio,
        ticker="AAPL",
        shares=5,
        current_price=150.0
    )
    assert updated_portfolio.loc[updated_portfolio["Ticker"] == "AAPL", "Shares"].iloc[0] == 15
    assert updated_portfolio.loc[updated_portfolio["Ticker"] == "AAPL", "Value"].iloc[0] == 2250.0
    assert updated_portfolio["Weight"].sum() == pytest.approx(1.0, rel=1e-3)

def test_edit_stock_existing(sample_portfolio):
    """Test editing the number of shares for an existing stock."""
    updated_portfolio = edit_stock(
        portfolio=sample_portfolio,
        ticker="MSFT",
        shares=10,
        current_price=210.0
    )
    assert updated_portfolio.loc[updated_portfolio["Ticker"] == "MSFT", "Shares"].iloc[0] == 10
    assert updated_portfolio.loc[updated_portfolio["Ticker"] == "MSFT", "Value"].iloc[0] == 2100.0
    assert updated_portfolio["Weight"].sum() == pytest.approx(1.0, rel=1e-3)

def test_edit_stock_nonexistent(sample_portfolio):
    """Test editing a non-existent stock."""
    updated_portfolio = edit_stock(
        portfolio=sample_portfolio,
        ticker="GOOG",
        shares=10,
        current_price=2800.0
    )
    assert "GOOG" not in updated_portfolio["Ticker"].values

def test_delete_stock_existing(sample_portfolio):
    """Test deleting an existing stock."""
    updated_portfolio = delete_stock(portfolio=sample_portfolio, ticker="AAPL")
    assert "AAPL" not in updated_portfolio["Ticker"].values
    assert updated_portfolio["Weight"].sum() == pytest.approx(1.0, rel=1e-3)

def test_delete_stock_nonexistent(sample_portfolio):
    """Test deleting a non-existent stock."""
    updated_portfolio = delete_stock(portfolio=sample_portfolio, ticker="GOOG")
    assert len(updated_portfolio) == len(sample_portfolio)

def test_calculate_weights(sample_portfolio):
    """Test weight calculation for a portfolio."""
    updated_portfolio = calculate_weights(sample_portfolio)
    total_value = sample_portfolio["Value"].sum()
    for _, row in updated_portfolio.iterrows():
        assert row["Weight"] == pytest.approx(row["Value"] / total_value, rel=1e-3)
    assert updated_portfolio["Weight"].sum() == pytest.approx(1.0, rel=1e-3)
