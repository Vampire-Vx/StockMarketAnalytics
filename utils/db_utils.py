import sqlite3
import pandas as pd

def create_database_connection(database_name: str) -> sqlite3.Connection:
    try:
        return sqlite3.connect(database_name, check_same_thread=False)
    except Exception as e:
        print(f"Error: {e}")
        return None

def is_table_empty(database_name: str, table_name: str) -> bool:
    try:
        with create_database_connection(database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            return count == 0
    except sqlite3.Error as e:
        print(f"Error checking table: {e}")
        return True

def populate_table_from_csv(database_name: str, csv_file: str, table_name: str) -> str:
    try:
        with create_database_connection(database_name) as conn:
            df = pd.read_csv(csv_file)
            if df.empty:
                return f"Error: The CSV file '{csv_file}' is empty."
            df.to_sql(table_name, conn, if_exists='replace', index=False)
        return 'Success'
    except Exception as e:
        return f'Error during table population: {e}'

def get_tickers_from_csv(csv_file: str) -> list:
    try:
        df = pd.read_csv(csv_file)
        return df['ticker'].dropna().unique().tolist()
    except Exception as e:
        print(f"Error reading tickers from CSV: {e}")
        return []