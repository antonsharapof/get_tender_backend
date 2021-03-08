from jose import jwt, JWTError
from passlib.hash import bcrypt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from settings import settings
from db.init_db import get_session, Session
from schemas import auth as auth_schema
from pydantic import ValidationError
from models import users as user_model
from datetime import datetime, timedelta
import sqlalchemy

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in')

def get_current_user(token: str = Depends(oauth2_scheme)) -> auth_schema.UserFullInfo:
    return AuthService.validate_token(token)


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    """Валидируем токен"""
    @classmethod
    def validate_token(cls, token: str) -> auth_schema.UserFullInfo:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credantials!!!',
            headers={
              'WWW-Authenticate': 'Bearer'
            },
        )
        try:
            """"Достаем полезную нагрузку из токена"""
            print(token)
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            raise exception from None

        user_data = payload.get('user')
        print(user_data)
        try:
            user = auth_schema.UserFullInfo.parse_obj(user_data)
        except ValidationError:
            raise exception

        return user

    @classmethod
    def create_token(cls, user: user_model.User) -> auth_schema.Token:
        user_data = auth_schema.UserFullInfo.from_orm(user)

        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expiration),
            'sub': str(user_data.id),
            'user': user_data.dict(),
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        return auth_schema.Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def register_new_user(self, user_data: auth_schema.UserCreate) -> auth_schema.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='This user already have an account  !!!',
            headers={
              'WWW-Authenticate': 'Bearer'
            })
        try:
            user = user_model.User(
                email=user_data.email,
                username=user_data.username,
                position=user_data.position,
                password_hash=self.hash_password(user_data.password)
            )
            self.session.add(user)
            self.session.commit()
        except sqlalchemy.exc.IntegrityError:
            raise exception

        return self.create_token(user)

    def authenticate_user(self, username: str, password: str) -> auth_schema.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={
              'WWW-Authenticate': 'Bearer'
            },
        )
        user = (
            self.session
                .query(user_model.User)
                .filter(user_model.User.username == username)
                .first()
        )

        if not user:
            raise exception
        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)
