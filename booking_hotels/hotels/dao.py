
from datetime import datetime

from sqlalchemy import and_, func, select

from booking_hotels.bookings.models import Bookings
from booking_hotels.dao.base import BaseDAO
from booking_hotels.database import async_sesion_maker
from booking_hotels.exception import HaveNoHotels
from booking_hotels.hotels.models import Hotels
from booking_hotels.hotels.rooms.models import Rooms


class HotelDAO(BaseDAO): 
    model = Hotels 

    @classmethod 
    async def find_all_hotels(cls) -> list[Hotels]:
        return await BaseDAO.find_all()
    
    @classmethod
    async def get_hotels(
    cls,
    location: str,
    date_from: str,
    date_to: str
): 
        async with async_sesion_maker() as session: # type: ignore
            # Получаем id отелей по местоположению
            hotels_ids = select(Hotels.id).where(Hotels.location.ilike(f"%{location}%"))
            hotels_ids = await session.execute(hotels_ids)
            hotels_ids = hotels_ids.scalars().all()

            # Если нет отелей, возвращаем пустой список
            if not hotels_ids:
                return HaveNoHotels

            # Получаем отели по их id
            hotels = await session.execute(select(Hotels).where(Hotels.id.in_(hotels_ids)))
            hotels = hotels.scalars().all()


            result = []
            for hotel in hotels:
                # Получаем номера отеля
                rooms = await session.execute(select(Rooms).where(Rooms.hotel_id == hotel.id))
                rooms = rooms.scalars().all()

                # Проверяем, есть ли хотя бы один свободный номер
                has_free_rooms = False
                for room in rooms:
                    bookings = await session.execute(
                        select(Bookings).filter(
                            Bookings.room_id == room.id,
                            Bookings.date_from <= datetime.fromisoformat(date_to).date(),
                            Bookings.date_to >= datetime.fromisoformat(date_from).date()
                        )
                    )
                    bookings = bookings.scalars().all()

                    if room.quantity - len(bookings) > 0:
                        has_free_rooms = True
                        break

                if has_free_rooms:
                    rooms_left = hotel.rooms_quantity - len(bookings) # type: ignore
                    hotel_data = {
                        "id": hotel.id,
                        "name": hotel.name,
                        "location": hotel.location,
                        "services": hotel.services,
                        "rooms_quantity": hotel.rooms_quantity,
                        "image_id": hotel.image_id,
                        "rooms_left": rooms_left
                    }

                    result.append(hotel_data) 

            return result

    @classmethod
    async def current_hotel(
        cls,
        hotel_id:int
        ):
        async with async_sesion_maker() as session: # type: ignore
            hotel=select(Hotels).where(Hotels.id==hotel_id)
            hotel = await session.execute(hotel)
            hotel= hotel.mappings().all()

            if not hotel:
                return HaveNoHotels

            return hotel
