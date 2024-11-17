
import json
from datetime import datetime

import pytest_asyncio
from sqlalchemy import insert

from booking_hotels.bookings.models import Bookings
from booking_hotels.config import settings
from booking_hotels.database import Base, async_sesion_maker, engine
from booking_hotels.hotels.models import Hotels
from booking_hotels.hotels.rooms.models import Rooms
from booking_hotels.main import app
from booking_hotels.users.models import Users


@pytest_asyncio.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"booking_hotels/tests/mock_{model}.json", "r") as file:
            return json.load(file)

    hotels = open_mock_json("hotels")
    rooms = open_mock_json("rooms")
    users = open_mock_json("users")
    bookings = open_mock_json("bookings")

    for booking in bookings:
        booking["date_from"] = datetime.strptime(booking["date_from"], "%Y-%m-%d")
        booking["date_to"] = datetime.strptime(booking["date_to"], "%Y-%m-%d")
        booking.pop("total_cost", None)
        booking.pop("total_days", None)

    async with async_sesion_maker() as session:
        await session.execute(insert(Hotels).values(hotels))
        await session.execute(insert(Rooms).values(rooms))
        await session.execute(insert(Users).values(users))
        await session.execute(insert(Bookings).values(bookings))

        await session.commit()
    yield print("True")


@pytest_asyncio.fixture(scope="function")
async def session():
    async with async_sesion_maker() as session:
        yield session

@pytest_asyncio.fixture(scope="function")
async def reset_users_table(session):
    await session.execute("TRUNCATE TABLE users RESTART IDENTITY CASCADE;")
    await session.commit()