import pytest

from app import app
from fastapi.testclient import TestClient


@pytest.fixture()
def client() -> TestClient:
    yield TestClient(app)
