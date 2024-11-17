from datetime import date

from fastapi import APIRouter, Depends
from pydantic import TypeAdapter

from booking_hotels.bookings.dao import BookingDAO
from booking_hotels.bookings.schemas import SBookings
from booking_hotels.exception import RoomCannotBeBooked
from booking_hotels.tasks.tasks import send_booking_confirmation_email
from booking_hotels.users.dependencies import get_current_user
from booking_hotels.users.models import Users
from fastapi_versioning import version

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)

model_adapter = TypeAdapter(SBookings)


@router.get("")
@version(1)
async def get_bookings(
    user: Users = Depends(get_current_user),
):  # -> list([SBookings]):
    return await BookingDAO.find_all(user_id=user.id)


@router.post("/")
@version(1)
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add_booking(room_id, date_from, date_to, user.id) # type: ignore

    if not booking:
        raise RoomCannotBeBooked

    booking_adapter = TypeAdapter(SBookings)
    booking_dict = booking_adapter.validate_python(booking).model_dump()
    send_booking_confirmation_email.delay(booking_dict, user.email) # type: ignore

    return booking_dict


@router.delete("/{booking_id}")
@version(1)
async def delete_bookings(booking_id: int, user: Users = Depends(get_current_user)):
    return await BookingDAO.DeleteB(booking_id, user.id) # type: ignore
