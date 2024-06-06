FROM python:alpine



RUN apk update && \
    apk add --no-cache gcc musl-dev libffi-dev postgresql-dev


COPY . .

RUN  pip install --no-cache-dir --upgrade -r requirements.txt


CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 3000"]
