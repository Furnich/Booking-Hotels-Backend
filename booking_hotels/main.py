
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
import time
from urllib.request import Request

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_versioning import VersionedFastAPI, version
from redis import asyncio as aioredis
from sqladmin import Admin
from prometheus_fastapi_instrumentator import Instrumentator

from booking_hotels.admin.auth import authentication_backend
from booking_hotels.admin.views import (
    BookingsAdmin,
    HotelsAdmin,
    RoomsAdmin,
    UsersAdmin,
)
from booking_hotels.bookings.router import router as router_bookings
from booking_hotels.config import settings
from booking_hotels.database import engine
from booking_hotels.hotels.rooms.router import router as router_rooms
from booking_hotels.hotels.router import router as router_hotels
from booking_hotels.images.router import router as router_images
from booking_hotels.pages.router import router as router_pages
from booking_hotels.users.router import router as router_users
from booking_hotels.importer.router import router as router_importer
from booking_hotels.logger import logger
from booking_hotels.prometheus.router import router as router_errors

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)

app.include_router(router_images)
app.include_router(router_pages)
app.include_router(router_importer)
app.include_router(router_errors)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","OPTIONS","DELETE","PATH","PUT"],
    allow_headers=["Content-Type", "Set-Cookie","Access-Control-Allow-Headers","Access-Control-Allow-Origin",
                    "Authorization"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info("Request execution time", extra={
        "process_time": round(process_time, 4)
        })
    return response

app = VersionedFastAPI(app,
    version_format='{major}',
    prefix_format='/v{major}',
)

instrumentator = Instrumentator(
    should_group_status_codes=False,
    excluded_handlers=[".*admin.*","/metrics"],
)
instrumentator.instrument(app).expose(app)


admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UsersAdmin)
admin.add_view(BookingsAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)

app.mount("/static",StaticFiles(directory="booking_hotels/static"), "static")
