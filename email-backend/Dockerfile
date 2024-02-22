FROM python:3.10-slim-buster
WORKDIR /app
COPY email-backend /app
RUN pip install --no-cache-dir -r /app/requirements.txt
ENTRYPOINT ["python3", "email-backend.py"]
