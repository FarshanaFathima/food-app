FROM python:3.10-slim-buster
WORKDIR /app
COPY api /app
RUN pip install --no-cache-dir -r /app/requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
