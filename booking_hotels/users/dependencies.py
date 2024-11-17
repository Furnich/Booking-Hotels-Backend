
from datetime import datetime, timezone

from fastapi import Depends, Request
from jose import JWTError, jwt

from booking_hotels.config import settings
from booking_hotels.exception import (
    IncorrectTokenFormatExcpetion,
    TokenAbsentException,
    TokenExpiredException,
    UserIsNotPresent,
)
from booking_hotels.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGHORITHM
        )
    except JWTError:
        raise IncorrectTokenFormatExcpetion
    
    expire: str = payload.get("exp")
    if (not expire) or (int(expire < datetime.now(timezone.utc).timestamp())):
        raise TokenExpiredException
    
    user_id: str = payload.get("sub")

    if not user_id:
        raise UserIsNotPresent
    
    user = await UsersDAO.find_by_id(int(user_id))
    
    if not user:
        raise UserIsNotPresent
    
    return user
