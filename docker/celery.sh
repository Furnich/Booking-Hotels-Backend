#!/bin/bash

if [[ "${1}" == "celery" ]]; then
    pipenv run celery --app=booking_hotels.tasks.celery:celery worker -l info
fi

if [[ "${1}" == "flower" ]]; then
    pipenv run celery --app=booking_hotels.tasks.celery:celery flower
fi