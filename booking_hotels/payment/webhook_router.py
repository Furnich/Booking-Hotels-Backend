from fastapi import APIRouter, HTTPException, Request

from cloudpayments import handle_cloudpayments_webhook


router = APIRouter(
    prefix="/payment",
    tags=["Payment"]
)

async def process_webhook(payload: dict) -> dict:
    """
    Общая функция для обработки webhook уведомлений от различных платёжных систем.

    :param payload: Данные уведомления от платёжной системы
    :return: Результат обработки уведомления
    """
    try:
            return await handle_cloudpayments_webhook(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка обработки Webhook'а: {str(e)}")


@router.post("/cloudpayments/webhook")
async def cloudpayments_webhook(request: Request):
    """
    Обрабатывает webhook уведомления от CloudPayments.

    :param request: Запрос от CloudPayments с данными уведомления
    :return: Статус и сообщение о результате обработки
    """
    payload = await request.json()
    result = await process_webhook(payload)
    return {"status": "Успешно", "message": result}