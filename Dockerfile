FROM python:3.9.12-alpine3.15
LABEL maintainer="luiztavares.dev"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./backend /backend

WORKDIR /backend
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update busybox-suid && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password backend
    
ENV PATH="/py/bin:$PATH"