
import asyncio
from datetime import datetime

from fastapi import APIRouter, Depends, Query
from fastapi_cache.decorator import cache

from booking_hotels.hotels.dao import HotelDAO
from booking_hotels.users.dependencies import get_current_user
from booking_hotels.users.models import Users



router = APIRouter(prefix="/hotels", tags=["Отели"]) 

@router.get("/") 
async def get_hotels(): 
    return await HotelDAO.find_all()

@router.get("/{locate}")
@cache(expire=20)
async def get_hotels_by_location(
    locate:str,
    date_from:str = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to:str = Query(..., description=f"Например, {datetime.now().date()}")
    ):
    await asyncio.sleep(2)
    return await HotelDAO.get_hotels(locate,date_from,date_to)

@router.get("/id/{id}")
async def get_current_hotel(hotel_id:int):
    return await HotelDAO.current_hotel(hotel_id)

@router.post("/{id}/post_review")
async def post_review(
        hotel_id:int,
        rating: int,
        text: str,
        user:Users = Depends(get_current_user),
    ):
    return await HotelDAO.post_review(hotel_id, rating, text, user)