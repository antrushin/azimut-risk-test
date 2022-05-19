from flask import Flask
import redis

redis_cache = redis.Redis(host='cache', port=6379, db=0)
redis_cache.set('myvariable', 'Hello world!')

app = Flask(__name__)

@app.route('/')
def get_myvariable():
    return redis_cache.get('myvariable')

