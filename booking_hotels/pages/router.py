
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from booking_hotels.hotels.router import get_hotels_by_location

router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]
)

templates = Jinja2Templates(directory="booking_hotels/templates")

@router.get("/hotels")
async def get_hotels_pages(
    request: Request,
    hotels=Depends(get_hotels_by_location)
):
    return templates.TemplateResponse(
        name="hotels.html",
        context={"request": request, "hotels": hotels}
    )
