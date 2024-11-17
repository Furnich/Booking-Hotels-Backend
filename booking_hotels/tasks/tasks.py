import csv
import smtplib
from pathlib import Path
from time import sleep

from PIL import Image
from pydantic import EmailStr

from booking_hotels.config import settings
from booking_hotels.tasks.celery import celery
from booking_hotels.tasks.email_templates import create_booking_confirmation_template


@celery.task
def process_picture(
    path:str,
):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized_1000 = im.resize((1000,500))
    im_resized_200 = im.resize((200,100))
    im_resized_1000.save(f"booking_hotels/static/images/resized_1000_{im_path.name}")
    im_resized_200.save(f"booking_hotels/static/images/resized_200_{im_path.name}")

@celery.task
def send_booking_confirmation_email(
    booking:dict,
    email_to: EmailStr,
):  
    sleep(10)
    email_to_mock = settings.SMTP_USER
    msg_content = create_booking_confirmation_template(booking, email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
