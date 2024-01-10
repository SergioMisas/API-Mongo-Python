FROM python:alpine3.19

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app/api.py .
CMD ["python", "api.py"]
