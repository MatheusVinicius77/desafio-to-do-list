FROM python:alpine



RUN apk update && \
    apk add --no-cache gcc musl-dev libffi-dev postgresql-dev

RUN mkdir -p /migrations/versions/

COPY . .



RUN  pip install --no-cache-dir --upgrade -r requirements.txt

# ENV PYTHONPATH=/app

CMD ["sh", "-c", "alembic revision --autogenerate && alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 3000"]
