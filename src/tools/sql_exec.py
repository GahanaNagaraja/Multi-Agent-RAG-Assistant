import duckdb, os
from src.app.settings import settings

_con = None

def connect():
    global _con
    if _con is None:
        os.makedirs("data", exist_ok=True)
        _con = duckdb.connect("file:app.db?cache=shared")
        _con.execute(f"CREATE OR REPLACE VIEW complaints AS SELECT * FROM read_csv_auto('{settings.TABLE_DIR}/complaints.csv');")
        _con.execute(f"CREATE OR REPLACE VIEW products   AS SELECT * FROM read_csv_auto('{settings.TABLE_DIR}/products.csv');")
    return _con

def run_sql(sql: str):
    con = connect()
    return con.execute(sql).fetch_df()

