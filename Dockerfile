FROM python:3.9-alpine
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

# install psycopg2 dependencies
RUN apk update --update-cache && \
    apk add --virtual .build-deps gcc musl-dev zlib-dev gettext-dev && \
    apk add python3 python3-dev libffi libffi-dev build-base \
            linux-headers pcre-dev

RUN apk add zlib-dev freetype-dev lcms2-dev tiff-dev tk-dev tcl-dev


# install dependencies
RUN python -m pip install -U pip
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt
COPY ./ /usr/src/app/

RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh"]