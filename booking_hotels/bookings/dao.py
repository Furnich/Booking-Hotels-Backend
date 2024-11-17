from datetime import date


from sqlalchemy import and_, delete, func, insert, or_, select
from sqlalchemy.exc import SQLAlchemyError

from booking_hotels.logger import logger
from booking_hotels.bookings.models import Bookings
from booking_hotels.bookings.schemas import BookingAdapter
from booking_hotels.dao.base import BaseDAO
from booking_hotels.database import async_sesion_maker
from booking_hotels.exception import HaveNoBooking
from booking_hotels.hotels.rooms.models import Rooms


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add_booking( 
        cls,
        room_id: int,
        date_from: date,
        date_to: date,
        user_id: int,
    ):

        booking_adapter = BookingAdapter()
        try:
            async with async_sesion_maker() as session:  # type: ignore # type: ignore
                booked_rooms = (
                    select(Bookings)
                    .where(
                        and_(
                            Bookings.room_id == room_id,
                            or_(
                                and_(
                                    Bookings.date_from >= date_from,
                                    Bookings.date_from <= date_to,
                                ),
                                and_(
                                    Bookings.date_from <= date_from,
                                    Bookings.date_to > date_from,
                                ),
                            ),
                        )
                    )
                    .cte("booked_rooms")
                )

                get_rooms_left = (
                    select(
                        (Rooms.quantity - func.count(booked_rooms.c.room_id)).label(
                            "rooms_left"
                        )
                    )
                    .select_from(Rooms)
                    .join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True)
                    .where(Rooms.id == room_id)
                    .group_by(Rooms.quantity, booked_rooms.c.room_id)
                )

                rooms_left = await session.execute(get_rooms_left)
                rooms_left = rooms_left.scalar()

                if rooms_left <= 0:
                    return None
                else:
                    get_price = select(Rooms.price).filter_by(id=room_id)
                    price = await session.execute(get_price)
                    price = price.scalar() 
                    add_booking = (
                        insert(Bookings)
                        .values(
                            room_id=room_id,
                            user_id=user_id,
                            date_from=date_from,
                            date_to=date_to,
                            price=price,
                        )
                        .returning(Bookings)
                    )

                    result = await session.execute(add_booking)
                    new_booking = result.scalar()

                    await session.commit()

                    new_booking_dict = new_booking.to_dict()
                    validated_booking = booking_adapter.validate_python(new_booking_dict)
                    return validated_booking
        except (SQLAlchemyError, Exception) as e:
            msg = ''
            if isinstance(e, SQLAlchemyError):
                msg = 'DataBase Exception'
            elif isinstance(e, Exception):
                msg = 'Unknown Exception'
            msg += ': Cannot add booking'
            extra = {
                "room_id": room_id,
                "date_from": date_from,
                "date_to": date_to,
                "user_id": user_id,
            }
            logger.error(
                msg, extra=extra, exc_info=True
            )


    @classmethod
    async def DeleteB(cls, booking_id: int, user_id: int):
        async with async_sesion_maker() as session: # type: ignore
            bookings = await session.execute(
                select(Bookings).where(Bookings.user_id == user_id)
            )
            bookings = bookings.scalars().all()
            if not bookings:
                raise HaveNoBooking

        try:
            booking = await session.get(Bookings, booking_id)
            if not booking:
                raise HaveNoBooking
        except:
            raise HaveNoBooking

        # Удаление бронирования
        await session.execute(delete(Bookings).where(Bookings.id == booking_id))
        await session.commit()
