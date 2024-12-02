from fastapi import Depends, Header

from booking_hotels.exception import TokenAbsentException

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
