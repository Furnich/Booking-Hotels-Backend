
from datetime import date

from fastapi import APIRouter

from booking_hotels.hotels.rooms.dao import RoomsDAO
from booking_hotels.hotels.rooms.models import Rooms

router = APIRouter(prefix="/hotels",tags=["Комнаты"])


@router.get("/{hotel_id}/rooms")
async def get_rooms(
    hotel_id: int,
    date_to:str,
    date_from:str
):
    result = await RoomsDAO.find_all_rooms_hotel(hotel_id,date_to,date_from)
    return result