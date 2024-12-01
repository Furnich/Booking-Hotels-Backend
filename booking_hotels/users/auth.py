from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from booking_hotels.config import settings
from booking_hotels.users.dao import UsersDAO
from booking_hotels.users.models import TokenData
from booking_hotels.exception import CannotContainUsername, TokenExpiredException

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_acces_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) +timedelta(minutes=120)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt

async def verify_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: Optional[str] = payload.get("sub")
        
        if username is None:
            raise CannotContainUsername
        return TokenData(username=username)
    except Exception as e:
        raise e


async def authenticate_user(email:EmailStr,password:str):
    user = await UsersDAO.find_one_or_none(email=email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user