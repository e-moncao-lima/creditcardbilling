from datetime import datetime
import pytest
from src.periodic_expenses.periodic_expenses import PeriodicExpense


@pytest.fixture
def periodic_expense() -> PeriodicExpense:
    return PeriodicExpense()

@pytest.fixture
def mock_expense():
    return {
        "name": "",
        "expense": "",
        "billing_day": ""
    }


def test_create_empty(periodic_expense, mock_expense) -> None:
    assert periodic_expense.create_periodic_expense(mock_expense) == None, "Empty input should create empty output"

def test_get_expenses_empty(periodic_expense) -> None:
    assert periodic_expense.get_periodic_expenses() == [], "It should get an empty list" 