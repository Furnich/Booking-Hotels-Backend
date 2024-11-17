from booking_hotels.dao.base import BaseDAO
from booking_hotels.users.models import Users


class UsersDAO(BaseDAO):
    model = Users
