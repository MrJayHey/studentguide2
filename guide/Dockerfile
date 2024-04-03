FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install gunicorn==20.1.0

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN chown -R nginx:nginx /app
RUN chmod -R 755 /app

ENTRYPOINT ["/entrypoint.sh"]