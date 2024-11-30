FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=config.settings.production

WORKDIR /app

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    python3-dev \
    postgresql-dev && \
    apk add --no-cache \
    bash \
    curl

RUN pip install --no-cache-dir poetry

COPY ../../pyproject.toml /app/

RUN poetry config virtualenvs.create false && \
     poetry install --only main --no-interaction --no-ansi

RUN apk del .build-deps

COPY ../../ /app

COPY ./prod.env /app/prod.env
ENV $(cat /app/prod.env | xargs)


EXPOSE 8000
