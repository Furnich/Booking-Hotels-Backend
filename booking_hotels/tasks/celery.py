from celery import Celery

from booking_hotels.config import settings

celery = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=["booking_hotels.tasks.tasks"]
)
