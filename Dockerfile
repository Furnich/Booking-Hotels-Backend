FROM python:3.12.4

RUN mkdir /booking

WORKDIR /booking

COPY requirements.txt .

RUN pip install pip --upgrade
RUN apt-get update && apt-get install -y netcat-openbsd
RUN pip install --default-timeout=100 -r requirements.txt

COPY . .

RUN chmod a+x /booking/docker/*.sh


CMD [ "gunicorn", "booking_hotels.main:app", "--workers", "1", "--worker-class", "uvicorn.worker.UvicornWorker", "--bind=0.0.0.0:8000" ]
