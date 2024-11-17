
import pytest
from httpx import ASGITransport, AsyncClient

from booking_hotels.main import app


@pytest.mark.parametrize("email,password,status_code", [
    ("test0k@example.com", "testik", 409),
    ("test0k@example.com", "testik", 409),
    ("dasdadadss", "testik", 422),
])
@pytest.mark.asyncio
async def test_register_user(reset_users_table, email,password,status_code):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/auth/register", json={
            "email": email,
            "password": password,
        })
        assert response.status_code == status_code

@pytest.mark.parametrize("email,password,status_code",[
    ("test0k@example.com", "testik", 200),
])
@pytest.mark.asyncio
async def test_login_user(email, password, status_code):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/auth/login", json={
            "email": email,
            "password":password
        })
        assert response.status_code == status_code