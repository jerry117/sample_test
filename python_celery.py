from ast import If
from unicodedata import name
from unittest import result
from black import main
from celery import Celery
# import celery
from flask import Flask
from celery import Celery

# ip = '172.63.11.57'
broker_url = 'redis://172.63.11.57:6379'
result_backend = 'redis://172.63.11.57:6379'

app = Flask(__name__)
celery_app = Celery(app.import_name, broker=broker_url, backend=result_backend)

@celery_app.task(name='demo/add')
def add(x, y):
    return x + y

@app.route('/add')
def index():
    result = add.delay(10, 20)
    print('--------------- 10 + 20 ----------------')
    return {'msg': 'success', 'result': result.wait()}


if __name__ == '__main__':
    app.run(debug=True)


# 安装
# pip install celery
# pip install redis
# pip install eventlet

# 先启动flask服务
# flask run
# 运行
# celery -A python_celery.celery_app worker -P eventlet -l info