from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import JSONB


class SHotels(BaseModel):
    id:int
    name:str
    locate:str
    services:JSONB
    rooms_quantity:int
    image_id:int

    class config:
        orm_mode = True 


class SReviews(BaseModel):
    id:int
    hotel_id:int
    user_id:int
    first_name:str
    last_name:str
    rating:int
    text:str
