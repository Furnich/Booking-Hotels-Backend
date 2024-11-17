import shutil

from fastapi import APIRouter, UploadFile

from booking_hotels.tasks.tasks import process_picture

router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"]
)


@router.post("/hotels")
async def add_hotel_image(name: int, file:UploadFile):
    im_path = f"booking_hotels/static/images/{name}.webp"
    with open(im_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_picture.delay(im_path) # type: ignore
