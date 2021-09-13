FROM python:3.8-slim

WORKDIR /app

COPY Pipfile.lock Pipfile /app/

RUN apt-get update && \
    apt-get install -y pipenv && \
    pipenv install --deploy --ignore-pipfile --system

COPY src/ entrypoint.sh /app/

ENTRYPOINT ["/app/entrypoint.sh"]
