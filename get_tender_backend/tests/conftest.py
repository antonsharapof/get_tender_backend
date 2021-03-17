from typing import Generator
import pytest
from get_tender_backend.db.init_db import Session
from fastapi.testclient import TestClient
from get_tender_backend.app import app
from get_tender_backend.models.users import User
from get_tender_backend.services.auth import AuthService
from get_tender_backend.tests.utils import get_random_account


@pytest.fixture(scope="session")
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture(scope="session")
def db() -> Generator:
    yield Session()


@pytest.fixture(scope="session")
def user_in_db(db: Session) -> Generator:
    user_data = get_random_account()
    service = AuthService()
    user = User(
        email=user_data['email'],
        username=user_data['username'],
        position=user_data['position'],
        password_hash=service.hash_password(user_data['password'])
    )
    db.add(user)
    db.commit()
    yield user_data
    db.delete(user)
    db.commit()

