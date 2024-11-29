from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    email: EmailStr
    Full_name: str
    password: str

class SUserAuth(BaseModel):
    email: EmailStr
    password: str