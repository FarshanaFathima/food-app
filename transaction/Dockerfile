FROM python:3.10-slim-buster
WORKDIR /app
COPY transaction /app
RUN pip install --no-cache-dir -r /app/requirements.txt
ENTRYPOINT ["python3","-u", "transaction.py"]
# ENTRYPOINT [ "ls" ]
