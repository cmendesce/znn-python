# Reference: https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
import os
import multiprocessing
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

loglevel = 'info'
workers = multiprocessing.cpu_count() * 2 + 1

def when_ready(server):
    GunicornPrometheusMetrics.start_http_server_when_ready(int(os.getenv('METRICS_PORT')))

def child_exit(server, worker):
    GunicornPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)