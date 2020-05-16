from flask import Flask
from znn.routes import znn
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

app = Flask(__name__, template_folder='znn/templates')
app.register_blueprint(znn)

# Add prometheus wsgi middleware to route /metrics requests
app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})