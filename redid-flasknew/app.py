from flask import Flask

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f"Hello, Docker Compose! This page has been viewed {count} times."

