FROM python:3.12-alpine3.19 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12-alpine3.19

RUN mkdir app

RUN python -m pip install --upgrade pip --no-cache-dir

COPY --from=requirements-stage /tmp/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt --no-cache-dir

COPY ./backend/. /app
