from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__,template_folder='templates')

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')

from app import routes
