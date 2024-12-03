from fastapi import APIRouter, HTTPException

from cloudpayments import create_payment as cloudpayments_create

import asyncio

router = APIRouter(
    prefix="/payment",
    tags=["Payment"]
)


async def create_payment_gateway(payment_function, amount: float, description: str) -> dict:
    """
    Асинхронно создает платеж через переданную платёжную систему.

    :param payment_function: Функция для создания платежа (например, yookassa_create)
    :param amount: Сумма платежа
    :param description: Описание платежа
    :return: Ответ от платёжной системы (например, JSON-ответ)
    :raises HTTPException: В случае ошибки при создании платежа
    """
    try:
        return await asyncio.to_thread(payment_function, amount, description)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error in payment gateway: {str(e)}")

@router.post("/cloudpayments")
async def create_cloudpayments_payment(amount: float, description: str) -> dict:
    return await create_payment_gateway(cloudpayments_create, amount, description)

