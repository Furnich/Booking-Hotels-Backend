from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    email: EmailStr
    First_name: str
    Last_name: str
    password: str

class SUserAuth(BaseModel):
    email: EmailStr
    password: str