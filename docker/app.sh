#!/bin/bash

pipenv run alembic upgrade head

pipenv run gunicorn booking_hotels.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000