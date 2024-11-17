
import pytest
from httpx import ASGITransport, AsyncClient

from booking_hotels.main import app


@pytest.mark.parametrize("room_id,date_from, date_to,status_code", [
    *[(3,"2030-05-01","2030-05-08", 200)]*19,
])
@pytest.mark.asycnio
async def test_add_and_get_booking(room_id,date_from, date_to,status_code):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        
        login_response = await client.post("/auth/login", json={
            "email": "test0k@example.com",
            "password": "testik"
        })
        assert login_response.status_code == 200
        print("тест кукки")
        
        assert "booking_access_token" in login_response.cookies
        print("тест кукки прошла")

        response = await client.post("/bookings/", params={
            "room_id": room_id,
            "date_from":date_from,
            "date_to":date_to,
        })

        assert response.status_code == status_code
