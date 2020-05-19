FROM python:3-alpine
RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev
RUN apk add --no-cache pcre
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir multiproc-tmp
ENV prometheus_multiproc_dir=/app/multiproc-tmp

ARG BUILDTIME_FIDELITY
ENV FIDELITY=$BUILDTIME_FIDELITY
COPY ./znn/images/$BUILDTIME_FIDELITY ./images/

COPY ./app.py .
COPY ./config.py .

COPY ./znn ./znn
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

ENV METRICS_PORT 9200
EXPOSE 5000
EXPOSE 9200

CMD gunicorn -c config.py -b 0.0.0.0:5000 app:app