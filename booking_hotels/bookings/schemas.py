from datetime import date

from pydantic import BaseModel, ValidationError


class SBookings(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class config:
        orm_mode = True


class BookingAdapter:
    @classmethod
    def validate_python(cls, data):
        try:
            return SBookings(**data)
        except ValidationError as e:
            print("Ошибка валидации:", e.errors())
            raise e
