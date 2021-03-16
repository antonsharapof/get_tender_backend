from fastapi.testclient import TestClient
from get_tender_backend.db.init_db import Session
from get_tender_backend.models.users import User
from get_tender_backend.tests.utils import get_random_account


def test_sign_up(client: TestClient, db: Session) -> None:
    account = get_random_account()
    response = client.post("/auth/sign-up", json=account)
    data = response.json()
    user_response = client.get("/auth/user", headers={'Authorization': f"Bearer {data.get('access_token')}"})
    user_data = user_response.json()
    db.query(User).filter(User.email == account.get('email')).delete()
    db.commit()
    assert response.status_code == 200
    assert type(data.get('access_token')) == str
    assert data.get('token_type') == 'bearer'
    assert user_response.status_code == 200
    assert user_data.get('email') == account.get('email')


def test_sign_in(client: TestClient, user_in_db: dict) -> None:
    account = {
        'email': user_in_db.get('email'),
        'password': user_in_db.get('password')
    }
    response = client.post("/auth/sign-in", json=account)
    data = response.json()
    user_response = client.get("/auth/user", headers={'Authorization': f"Bearer {data.get('access_token')}"})
    user_data = user_response.json()
    assert response.status_code == 200
    assert user_data.get('email') == account.get('email')
