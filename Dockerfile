FROM python:3.7-slim-stretch

RUN apt-get update \
    && apt-get install -y gcc \
    && pip install pipenv

COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock

RUN pipenv lock -r > requirements.txt \
    && pipenv lock -r -d > requirements-dev.txt \
    && pip install -r requirements.txt \
    && pip install -r requirements-dev.txt

## create a user
RUN useradd app && mkdir /home/app \
    && chown app:app /home/app

USER app
WORKDIR /home/app

ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
