FROM python:3.10.4-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]
LABEL author="Bykov Evgeniy" version=1 release_date=17-08-2022
