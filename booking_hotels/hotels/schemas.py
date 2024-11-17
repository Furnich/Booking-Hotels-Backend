
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