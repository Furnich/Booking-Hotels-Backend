
import asyncio
from datetime import datetime

from fastapi import APIRouter, Query
from fastapi_cache.decorator import cache

from booking_hotels.hotels.dao import HotelDAO



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
    await asyncio.sleep(3)
    return await HotelDAO.get_hotels(locate,date_from,date_to)

@router.get("/id/{id}")
async def get_current_hotel(hotel_id:int):
    return await HotelDAO.current_hotel(hotel_id)