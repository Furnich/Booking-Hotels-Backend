FROM python:3.12.4

RUN mkdir /booking

WORKDIR /booking

COPY Pipfile Pipfile.lock ./

RUN pip install --upgrade pip && \
    pip install pipenv
RUN apt-get update && apt-get install -y netcat-traditional
RUN pipenv install --deploy --ignore-pipfile
RUN if [ "$(uname)" = "Linux" ]; then echo "Skipping pywin32 installation on Linux"; else pip install pywin32; fi

COPY . .

RUN chmod a+x /booking/docker/*.sh


CMD [ "gunicorn", "booking_hotels.main:app", "--workers", "1", "--worker-class", "uvicorn.worker.UvicornWorker", "--bind=0.0.0.0:8000" ]
