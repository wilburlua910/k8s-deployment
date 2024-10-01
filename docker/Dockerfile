FROM python:3.9.20-alpine
WORKDIR /app
COPY . /app/

RUN pip3 install --no-cache-dir -r requirements.txt &&\
    apk update && apk add curl

CMD ["python", "main.py"]