#Uses Python 3.13
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y iputils-ping && pip install -r requirements.txt

COPY . . 

EXPOSE 5000

CMD ["flask","--app","app","run","--host=0.0.0.0","--port=5000"]