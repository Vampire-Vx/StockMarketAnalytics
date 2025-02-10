import pandas as pd
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor
from config import DATABASE_URL, STOCKS_SECTOR_CSV_PATH
import utils.db_utils as db

def fetch_stock_data(ticker: str, period: str = 'max', interval: str = '1d') -> pd.DataFrame:
    try:
        data = yf.download(ticker, period=period, interval=interval)
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [col[0] for col in data.columns]
        data.reset_index(inplace=True)
        data['ticker'] = ticker
        return data
    except Exception as e:
        print(f"Error during data fetch for {ticker}: {e}")
        return None

def save_data_to_database(database_name: str, data: pd.DataFrame, table_name: str = "stock_prices") -> str:
    if data is None or data.empty:
        return "No data to save."
    try:
        with db.create_database_connection(database_name) as conn:
            existing_dates = pd.read_sql_query(
                f"SELECT date FROM {table_name} WHERE ticker='{data['ticker'][0]}'", conn
            )
            data['Date'] = pd.to_datetime(data['Date'])
            existing_dates['date'] = pd.to_datetime(existing_dates['date'])
            data = data[~data['Date'].isin(existing_dates['date'])]
            if data.empty:
                return "No new data to insert."
            data.rename(columns={
                'Date': 'date',
                'Adj Close': 'adj_close',
                'Close': 'close',
                'High': 'high',
                'Low': 'low',
                'Open': 'open',
                'Volume': 'volume'
            }, inplace=True)
            data.to_sql(table_name, conn, if_exists='append', index=False)
        return 'Success'
    except Exception as e:
        return f'Error during data save: {e}'

def fetch_all_tickers(tickers: list, database_name: str) -> None:
    for ticker in tickers:
        try:
            data = fetch_stock_data(ticker)
            result = save_data_to_database(database_name, data)
            print(f"{ticker}: {result}")
        except Exception as e:
            print(f"Error processing {ticker}: {e}")

def fetch_all_tickers_multithread(tickers: list, database_name: str) -> None:
    def process_ticker(ticker):
        try:
            data = fetch_stock_data(ticker)
            result = save_data_to_database(database_name, data)
            print(f"{ticker}: {result}")
        except Exception as e:
            print(f"Error processing {ticker}: {e}")

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_ticker, tickers)

def update_db():
    database_name = DATABASE_URL
    csv_file = STOCKS_SECTOR_CSV_PATH
    tickers = db.get_tickers_from_csv(csv_file)
    fetch_all_tickers(tickers, database_name)

if __name__ == "__main__":
    update_db()
