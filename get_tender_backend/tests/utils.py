import random
import string

from get_tender_backend.db.init_db import Session
from get_tender_backend.models.users import User
from get_tender_backend.services.auth import AuthService


def get_random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=10))


def get_random_email() -> str:
    return f"{get_random_lower_string()}@{get_random_lower_string()}.com"


def get_random_account() -> dict:
    email = get_random_email()
    username = get_random_lower_string()
    position = get_random_lower_string()
    password = get_random_lower_string()
    account = {
        'email': email,
        'username': username,
        'position': position,
        'password': password
    }
    return account


def create_user_in_db(user_data: dict, service: AuthService, db: Session):
    user = User(
        email=user_data['email'],
        username=user_data['username'],
        position=user_data['position'],
        password_hash=service.hash_password(user_data['password'])
    )
    db.add(user)
    db.commit()