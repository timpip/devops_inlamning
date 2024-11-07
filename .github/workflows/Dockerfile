FROM python:latest

COPY requirements.txt /app/

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
