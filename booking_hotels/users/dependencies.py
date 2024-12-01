
from datetime import datetime, timezone

from fastapi import Depends, Header, Request
from jose import JWTError, jwt
import logging

from booking_hotels.config import settings
from booking_hotels.exception import (
    IncorrectTokenFormatExcpetion,
    TokenAbsentException,
    TokenExpiredException,
    UserIsNotPresent,
)
from booking_hotels.users.dao import UsersDAO

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def get_token(authorization: str = Header(None)):
    print(f"Authorization header: {authorization}")
    if authorization is None:
        raise TokenAbsentException

    token = authorization.split(" ")[1] if " " in authorization else authorization
    return token

async def get_current_user(token: str = Depends(get_token)):
    from booking_hotels.users.auth import verify_token
    try:
        user = await verify_token(token)
        return user
    except Exception as e:
        raise e

'''
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenFormatExcpetion
    
    expire: str = payload.get("exp") or "None"
    if (not expire) or (int(expire) < datetime.now(timezone.utc).timestamp()):
        raise TokenExpiredException
    
    user_id: str = payload.get("sub") or "None"
    if not user_id:
        raise UserIsNotPresent
    
    user = await UsersDAO.find_by_id(int(user_id))  
    if not user:
        raise UserIsNotPresent
    return user
'''
