from fastapi import APIRouter, Depends, Response

from booking_hotels.exception import (
    IncorrectEmailOrPasswordException,
    UserAlreadyExistsException,
)
from booking_hotels.users.auth import (
    authenticate_user,
    create_acces_token,
    get_password_hash,
)
from booking_hotels.users.dao import UsersDAO
from booking_hotels.users.dependencies import get_current_user
from booking_hotels.users.models import Users
from booking_hotels.users.schemas import SUserAuth, SUserRegister

router = APIRouter(
    prefix="",
    tags=["Auth & Пользователи"]
)

@router.post("/auth/register")
async def register_user(user_data:SUserRegister):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email,hashed_password=hashed_password)


@router.post("/auth/login")
async def login_user(response:Response, user_data:SUserAuth):
    user = await authenticate_user(user_data.email,user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_acces_token({"sub":str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token


@router.post("/user/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")

@router.get("/user/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user
