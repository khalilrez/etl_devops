FROM python:3.10-alpine

COPY requirements.txt /

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 8001

CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]