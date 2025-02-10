import os
from config import DATABASE_URL, STOCKS_SECTOR_CSV_PATH
from scripts.update_db import update_db
import utils.db_utils as db

def create_tables(database_name: str) -> str:
    try:
        with db.create_database_connection(database_name) as conn:
            # Create stock_prices table
            conn.execute("""
            CREATE TABLE IF NOT EXISTS stock_prices (
                id INTEGER PRIMARY KEY,
                date DATE,
                adj_close REAL,
                close REAL,
                high REAL,
                low REAL,
                open REAL,
                volume INTEGER,
                ticker TEXT
            )
            """)
            # Create stock_sector table
            conn.execute("""
            CREATE TABLE IF NOT EXISTS stock_sector (
                ticker TEXT PRIMARY KEY,
                sector TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
        return 'Success'
    except Exception as e:
        return f'Error during tables creation: {e}'

def init_db(database_name: str, csv_file: str) -> str:
    tickers = db.get_tickers_from_csv(csv_file)
    if not tickers:
        return "Error: No tickers found in CSV file."

    if not os.path.exists(database_name):
        print("Database file not found. Initializing database...")
        table_creation_result = create_tables(database_name)
        if table_creation_result == 'Success':
            print("Tables created successfully.")

            # Populate stock_sector table
            print("Populating stock_sector table with sector data...")
            sector_result = db.populate_table_from_csv(database_name, csv_file, "stock_sector")
            print(sector_result)

            # Populate stock_prices table
            print("Populating stock_prices table with initial data...")
            update_db()

            return "Database initialized and tables populated."
        else:
            return table_creation_result
    else:
        print("Database file already exists.")

        # Check and populate stock_sector table if empty
        if db.is_table_empty(database_name, "stock_sector"):
            print("Table 'stock_sector' is empty. Populating with sector data...")
            sector_result = db.populate_table_from_csv(database_name, STOCKS_SECTOR_CSV_PATH, "stock_sector")
            print(sector_result)

        # Check and populate stock_prices table if empty
        if db.is_table_empty(database_name, "stock_prices"):
            print("Table 'stock_prices' is empty. Populating with initial data...")
            update_db()

        return "Database and tables already exist and are populated."

if __name__ == "__main__":
    print(init_db(DATABASE_URL, STOCKS_SECTOR_CSV_PATH))
