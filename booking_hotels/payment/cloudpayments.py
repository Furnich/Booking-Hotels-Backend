'''
Код с подключением CloudPayments
'''

import requests
from booking_hotels.database import async_session_maker
from booking_hotels.config import settings
from booking_hotels.payment.models import Payments


async def create_payment(amount: float, description: str, order_id: str):
    """
    Создание платежа через API CloudPayments.

    :param amount: Сумма платежа в рублях.
    :param description: Описание платежа.
    :param order_id: Уникальный идентификатор заказа.
    :return: Ответ от CloudPayments (JSON).
    """

    url = "https://api.cloudpayments.ru/payments"
    headers = {
        "Authorization": f"Bearer {settings.CLOUDPAYMENTS_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "amount": amount,
        "currency": "RUB",
        "description": description,
        "order_id": order_id,
        "return_url": "https://yourwebsite.com/payment/return",
        "invoice_id": f"inv_{order_id}",
        "payment_type": "BANK_CARD",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:

            async with async_session_maker() as session: # type: ignore

                new_payment = Payments(
                    amount=amount,
                    currency="RUB",
                    description=description,
                    order_id=order_id,
                    invoice_id=f"ing_{order_id}",
                    payment_type="BANK_CARD",
                )
                session.add(new_payment)
                await session.commit()

                return response.json()
        else:
            return {"error": "Ошибка создания платежа", "details": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": "Запрос не выполнен", "details": str(e)}

async def handle_cloudpayments_webhook(payload: dict) -> dict:
    """
    Обработка webhook уведомления

    :param payload: Данные уведомления 
    :return: Результат обработки уведомления
    """
    async with async_session_maker() as session: # type: ignore
        if payload.get("event") == "payment.succeeded":

            payment_id = payload.get("data").get("transactionId") # type: ignore
            payment = session.query(Payments).filter(Payments.invoice_id == payment_id).first()

            if payment:
                payment.status = "succeeded"
                session.commit()
            return {"status": "Обработанный", "message": "Платеж успешно выполнен"}

        elif payload.get("event") == "payment.failed":
            payment_id = payload.get("data").get("transactionId") # type: ignore # type: ignore
            payment = session.query(Payments).filter(Payments.invoice_id == payment_id).first()
            if payment:
                payment.status = "failed"
                session.commit()
            return {"status": "Обработанный", "message": "Платеж не выполнен"}

        elif payload.get("event") == "payment.cancelled":
            payment_id = payload.get("data").get("transactionId") # type: ignore
            payment = session.query(Payments).filter(Payments.invoice_id == payment_id).first()
            if payment:
                payment.status = "cancelled"
                session.commit()
            return {"status": "Обработан", "message": "Платеж отменен"}

        return {"status": "ignored", "message": "Event not handled"}
