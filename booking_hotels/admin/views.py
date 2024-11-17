
from sqladmin import ModelView

from booking_hotels.bookings.models import Bookings
from booking_hotels.hotels.models import Hotels
from booking_hotels.hotels.rooms.models import Rooms
from booking_hotels.users.models import Users


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email, Users.booking]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class BookingsAdmin(ModelView, model=Bookings):
    column_list = [c.name for c in Bookings.__table__.c] + [Bookings.user, Bookings.room]
    can_delete = True
    name = "Бронь"
    name_plural = "Брони"
    icon = "fa-solid fa-book"

class HotelsAdmin(ModelView, model=Hotels):
    column_list = [c.name for c in Hotels.__table__.c] + [Hotels.room]
    can_delete = True
    name = "Отель"
    name_plural = "Отели"
    icon = "fa-solid fa-hotel"

class RoomsAdmin(ModelView, model=Rooms):
    column_list = [c.name for c in Rooms.__table__.c] + [Rooms.hotel, Rooms.booking]
    can_delete = True
    name = "Номер"
    name_plural = "Номера"
    icon = "fa-solid fa-bed"