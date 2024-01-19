import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture()
def client() -> TestClient:
    yield TestClient(app)
