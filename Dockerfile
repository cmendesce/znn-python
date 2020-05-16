FROM python:3-alpine
RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev
RUN apk add --no-cache pcre
WORKDIR /app

ARG BUILDTIME_FIDELITY
ENV FIDELITY=$BUILDTIME_FIDELITY
COPY ./znn/images/$BUILDTIME_FIDELITY ./images/

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app.py .
COPY ./znn ./znn
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
EXPOSE 5000

CMD ["uwsgi", "--http", "0.0.0.0:5000", "--wsgi-file", "/app/app.py", "--callable", "app_dispatch"]