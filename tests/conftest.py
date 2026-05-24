import os
import sys
import pytest
from fastapi.testclient import TestClient

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
BACKEND_DIR = os.path.join(ROOT_DIR, "backend")
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from api.routes import api_router
from main import app

@pytest.fixture
def client():
    app.include_router(api_router)
    return TestClient(app)


@pytest.fixture
def test_client(client):
    return client
