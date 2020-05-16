import base64
import time
import os
from flask import current_app as app
from flask import Flask, Blueprint, render_template, request, jsonify
from prometheus_client import Summary, Histogram
from .db import find_random_news, count_news

znn = Blueprint('znn', __name__)
REQUEST_TIME = Histogram('znn_request_latency_seconds', 'Description of histogram')
PARSE_IMAGE_TIME = Histogram('znn_parse_image_time_seconds', 'Description of histogram')
DATABASE_TIME = Histogram('znn_database_time_seconds', 'Description of histogram')

@REQUEST_TIME.time()
@znn.route('/news')
def news():
    render_time = time.time()
    start_time = time.time()
    news = find_random_news()
    DATABASE_TIME.observe(time.time() - start_time)
    fidelity = os.getenv('FIDELITY', 'text')

    if fidelity != 'text':
        start_time = time.time()
        with open(f'{os.getcwd()}/{news["image_path"]}', 'rb') as img_file:
            image = base64.b64encode(img_file.read())
            news['image_base64'] = image.decode('utf-8')
            PARSE_IMAGE_TIME.observe(time.time() - start_time)

    render_time = time.time() - render_time
    headers = [('fidelity', str(fidelity)), ('render_time', str(render_time))]
    return render_template('news.html', news=news, render_time=render_time, fidelity=fidelity), headers


@znn.route('/readiness')
def readiness():
    count_news()
    return 'ok'

@znn.route('/liveness')
def liveness():
    return 'ok'