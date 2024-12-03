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
    """
    Функция на получение всех букингов пользователя

    :params user: Получение данных юзера функцией get_current_user
    :return: список букингов
    """
    return await BookingDAO.find_all(user_id=user.id)


@router.post("/")
@version(1)
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user),
):
    """
    Функция добавляет букинг и одновременно проверяет, на возможность
    бронирования номерв
    
    :param room_id: ID номера
    :param date_from: Дата заезда
    :param date_to: Дата выезда
    :params user: Получение данных юзера функцией get_current_user
    :result: данные о бронирование
    """
    booking = await BookingDAO.add_booking(room_id, date_from, date_to, user.id) # type: ignore

    if not booking:
        raise RoomCannotBeBooked

    booking_adapter = TypeAdapter(SBookings)
    booking_dict = booking_adapter.validate_python(booking).model_dump()
    send_booking_confirmation_email.delay(booking_dict, user.email) # type: ignore

    return booking_dict


@router.delete("/{booking_id}")
@version(1)
async def delete_bookings(
    booking_id: int,
    user: Users = Depends(get_current_user)
    ):
    """
    Функция удаляет букинг
    
    :param booking_id: ID букинга
    :params user: Получение данных юзера функцией get_current_user
    "return" None или ошибку
    """
    return await BookingDAO.DeleteB(booking_id, user.id) # type: ignore
