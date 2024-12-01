from datetime import datetime

from fastapi import Query
from sqlalchemy import select

from booking_hotels.bookings.models import Bookings
from booking_hotels.dao.base import BaseDAO
from booking_hotels.database import async_session_maker
from booking_hotels.hotels.rooms.models import Rooms


class RoomsDAO(BaseDAO):
    model = Rooms


    @classmethod

    async def find_all_rooms_hotel(
        cls,
        hotel_id: int,
        date_from: str = Query(..., description="Дата начала бронирования"),
        date_to: str = Query(..., description="Дата окончания бронирования"),

    ):
        """
        Args:
            hotel_id: ID отеля.
            date_from: Дата начала бронирования.
            date_to: Дата окончания бронирования.
            db_session: Асинхронная сессия базы данных.

        Returns:
            Список словарей, где каждый словарь представляет номер:
            - id: ID номера.
            - hotel_id: ID отеля.
            - name: Название номера.
            - description: Описание номера.
            - services: Услуги в номере.
            - price: Цена за ночь.
            - quantity: Количество номеров.
            - image_id: ID изображения номера.
            - total_cost: Стоимость бронирования номера за весь период.
            - rooms_left: Количество оставшихся номеров.
        """


        date_from = datetime.fromisoformat(date_from) # type: ignore
        date_to = datetime.fromisoformat(date_to) # type: ignore

        async with async_session_maker() as session: # type: ignore
            rooms = await session.execute(select(Rooms).filter_by(hotel_id=hotel_id))
            rooms = rooms.scalars().all()

            result = []
            
            for room in rooms:
                bookings = await session.execute(
                    select(Bookings).filter(
                        Bookings.room_id == room.id,
                        Bookings.date_from <= date_to,
                        Bookings.date_to >= date_from
                    )
                )
                bookings = bookings.scalars().all()

                rooms_left = room.quantity - len(bookings)

                total_cost = room.price * (date_to - date_from).days # type: ignore

                room_data = {
                    "id": room.id,
                    "hotel_id": room.hotel_id,
                    "name": room.name,
                    "description": room.description,
                    "services": room.services,
                    "price": room.price,
                    "quantity": room.quantity,
                    "image_id": room.image_id,
                    "total_cost": total_cost,
                    "rooms_left": rooms_left
                }
                result.append(room_data)

            return result


"""
в ЬД нет таблицы ревьюсь
"""