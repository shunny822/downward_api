FROM python:3.9-slim

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY . /app

RUN pip install flask

CMD ["python", "app.py"]