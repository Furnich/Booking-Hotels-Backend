
from datetime import datetime

import pytest

from booking_hotels.bookings.dao import BookingDAO


@pytest.mark.asyncio
async def test_add_and_get_booking():
    new_booking = await BookingDAO.add(
        user_id=2,
        room_id=2,
        date_from=datetime.strptime("2024-06-15", "%Y-%m-%d"),
        date_to=datetime.strptime("2024-06-19", "%Y-%m-%d"),
    )

    assert new_booking.user_id ==2
    assert new_booking.room_id ==2


    await BookingDAO.find_by_id(new_booking.id)

    assert new_booking is not None
    