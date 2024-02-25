FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install gunicorn==20.1.0

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]