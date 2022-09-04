from datetime import datetime
import sqlite3
import pandas as pd


class PeriodicExpense:
    def __init__(self, db_conn: sqlite3.Connection) -> None:
        self.db_conn = db_conn

    def create_periodic_expense(self, name: str, 
        expense: float, billing_day: datetime) -> None:
        pass

    def get_periodic_expenses(self) -> pd.DataFrame:
        return []
