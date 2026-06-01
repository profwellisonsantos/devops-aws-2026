from flask import Flask
from redis import Redis

app = Flask(__name__)
cache = Redis(host='redis', port=6379) 

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f'Olá! Esta página foi vista {count} vezes.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)