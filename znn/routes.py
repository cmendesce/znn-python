import base64
import time
import os
from flask import current_app as app
from flask import Flask, Blueprint, Response, render_template, request, jsonify
from prometheus_client import Histogram
from prometheus_client import multiprocess, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST

from .db import find_random_news, count_news

znn = Blueprint('znn', __name__)
PARSE_IMAGE_TIME = Histogram('znn_parse_image_time_seconds', 'ZNN parse image duration in second')
DATABASE_TIME = Histogram('znn_database_time_seconds', 'ZNN database query duration in second')

@znn.route('/news')
def news():
    render_time = time.time()
    
    db_time = time.time()
    news = find_random_news()
    db_time = time.time() - db_time
    DATABASE_TIME.observe(db_time)
    
    fidelity = os.getenv('FIDELITY', '200k')

    parse_time = 0
    if fidelity != 'text':
        parse_time = time.time()
        with open(f'{os.getcwd()}/{news["img_res"]}', 'rb') as img_file:
            image = base64.b64encode(img_file.read())
            news['image_base64'] = image.decode('utf-8')
            parse_time = time.time() - parse_time
            PARSE_IMAGE_TIME.observe(parse_time)

    render_time = time.time() - render_time
    headers = [
        ('fidelity', str(fidelity)), 
        ('render-time', str(render_time)),
        ('parse-time', str(parse_time)),
        ('db-time', str(db_time))
    ]
    
    return render_template('news.html', news=news, render_time=render_time, fidelity=fidelity), headers


@znn.route('/readiness')
def readiness():
    count_news()
    return 'ok'

@znn.route('/liveness')
def liveness():
    return 'ok'

@znn.route("/metrics")
def metrics():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)