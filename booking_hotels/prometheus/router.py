from random import random
import time

from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/prometheus",
    tags=["Тестирование Granfa + Prometheus"]
)


@router.get("/get_error")
def get_error():
    try:
        if random() > 0.5:
            raise ZeroDivisionError("Деление на ноль")
        else:
            raise KeyError("Ключ не найден")
    except ZeroDivisionError as e:
        # Обработка ZeroDivisionError
        raise HTTPException(status_code=400, detail=str(e))
    except KeyError as e:
        # Обработка KeyError
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/time_consumer")
def time_consumer():
    time.sleep(random()*5)
    return 1

@router.get("/memoru_consumer")
def memory_consumer():
    _ = {i for i in range(10000000)}
    return 1

