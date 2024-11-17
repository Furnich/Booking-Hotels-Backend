import csv
import io
from booking_hotels.config import settings

import psycopg2
from fastapi import APIRouter, Depends, UploadFile

from booking_hotels.users.dependencies import get_current_user
from booking_hotels.users.models import Users



router = APIRouter(prefix="/import", tags=["Импорт csv файла"])

@router.post("/{table_name}")
async def import_csv(table_name:str, file:UploadFile,user: Users = Depends(get_current_user)):
    conn = psycopg2.connect(
        f"host={settings.DB_HOST} port={settings.DB_PORT} dbname={settings.DB_NAME} user={settings.DB_USER} password={settings.DB_PASS}"\
    )
    cur = conn.cursor()

    try:
        with io.TextIOWrapper(file.file, encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cur.execute(
                f"INSERT INTO {table_name} VALUES {*row,}"
                )
            conn.commit()

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    
    finally:
        cur.close()
        conn.close()

