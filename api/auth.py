from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from schemas.auth import (
    UserCreate,
    Token
)
from services.auth import AuthService, get_current_user
from schemas.auth import User, UserFullInfo, UserLogin

router = APIRouter(
    prefix='/auth',
    tags= ['auth'],
)

@router.post('/sign-up', response_model=Token)
def sing_up(user_data: UserCreate,
    service: AuthService = Depends(AuthService)):
    return service.register_new_user(user_data)

@router.post('/sign-in', response_model=Token)
# def sing_in(form_data: OAuth2PasswordRequestForm = Depends(),
#     service: AuthService = Depends(AuthService)):
#     print(form_data.username, form_data.password)
#     return service.authenticate_user(
#         form_data.username,
#         form_data.password
#     )
def sing_in(form_data: UserLogin, service: AuthService = Depends(AuthService)):
    print(form_data.email, form_data.password)
    return service.authenticate_user(
        form_data.email,
        form_data.password
    )

@router.get('/user', response_model=UserFullInfo)
def get_user(user: User = Depends(get_current_user)):
    return user