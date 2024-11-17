
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import JSONB


class SRooms(BaseModel):
    id:int
    hotel_id:int
    name:str
    description:str
    price:int
    services:JSONB
    quantity:int
    image_id:int

    class config:
        orm_mode = True 