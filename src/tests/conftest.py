"""Added test."""
from app.main import app
import pytest 


@pytest.fixture()
def client():
    """Fixture"""
    return app.test_client()
