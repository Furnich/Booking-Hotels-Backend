from email.message import EmailMessage

from pydantic import EmailStr

from booking_hotels.config import settings


def create_booking_confirmation_template(
    booking: dict,
    email_to: EmailStr,
):
    # Проверка на наличие необходимых ключей в словаре booking
    required_keys = ["date_from", "date_to", "room_id", "user_id", "total_cost"]
    for key in required_keys:
        if key not in booking:
            raise ValueError(f"Отсутсвует необходимая информация: {key}")

    email = EmailMessage()
    
    email["Subject"] = "Подтверждение Бронирования"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Подтверждение бронирования</h1>
            <p>Вы забронировали номер в отеле с <strong>{booking["date_from"]}</strong> по <strong>{booking["date_to"]}</strong>.</p>
            <p>Номер комнаты: <strong>{booking["room_id"]}</strong></p>
            <p>Идентификатор пользователя: <strong>{booking["user_id"]}</strong></p>
            <p>Общая стоимость: <strong>{booking["total_cost"]} руб.</strong></p>
        """,
        subtype="html"
    )
    
    return email
