from flask import Flask
from znn.routes import znn

from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

app = Flask(__name__, template_folder='znn/templates')
app.register_blueprint(znn)

metrics = GunicornPrometheusMetrics(app)

if __name__ == '__main__':
    app.run(debug=False, port=5000)