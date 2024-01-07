FROM python:3.11.7
WORKDIR /backend
ENV DATABASE_URL=postgresql://wbjhrcfk:Oh9-0QvWApeqi6OWNFirgsWeCBWH3_iE@tiny.db.elephantsql.com/wbjhrcfk

COPY . /backend/

RUN poetry run install