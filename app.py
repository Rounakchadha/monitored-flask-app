
from flask import Flask, Response, render_template_string, request
import time
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

# Prometheus Metrics
REQUEST_COUNT = Counter('app_request_count', 'Total web app request count', ['method', 'endpoint'])
EXCEPTION_COUNT = Counter('app_exception_count_total', 'Total exceptions count')
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency', ['endpoint'])

start_time = time.time()

@app.route('/')
def index():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Monitored Flask App</title>
            <style>
                body {
                    font-family: sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding-top: 50px;
                }
                .container {
                    background-color: white;
                    border-radius: 10px;
                    padding: 30px;
                    width: 400px;
                    margin: auto;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }
                h1 { color: #333; }
                .btn {
                    margin: 10px;
                    padding: 10px 20px;
                    font-size: 16px;
                    background-color: #2979ff;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                .btn:hover {
                    background-color: #005ecb;
                }
                .section {
                    margin-top: 20px;
                    font-size: 18px;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>📈 Monitored Flask App</h1>
                <h3>Real-time DevOps Dashboard</h3>
                <div class="section">
                    <p><b>Total Requests:</b> {{ total }}</p>
                    <p><b>Total Exceptions:</b> {{ exceptions }}</p>
                    <p><b>Uptime:</b> {{ uptime }} seconds</p>
                </div>
                <a href="/" class="btn">Simulate Request</a>
                <a href="/fail" class="btn">Simulate Error</a>
                <a href="/metrics" class="btn">View Metrics</a>
            </div>
        </body>
        </html>
    """, total=REQUEST_COUNT.labels(method='GET', endpoint='/')._value.get(),
         exceptions=EXCEPTION_COUNT._value.get(),
         uptime=round(time.time() - start_time, 2)
    )

@app.route('/fail')
def fail():
    REQUEST_COUNT.labels(method='GET', endpoint='/fail').inc()
    EXCEPTION_COUNT.inc()
    raise Exception("Intentional Failure")

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

@app.before_request
def before_request():
    request._start_time = time.time()

@app.after_request
def after_request(response):
    latency = time.time() - request._start_time
    endpoint = request.endpoint if request.endpoint else "unknown"
    REQUEST_LATENCY.labels(endpoint=f"/{endpoint}").observe(latency)
    return response

if __name__ == '__main__':
    app.run(port=5001)
