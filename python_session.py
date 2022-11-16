from flask import Flask, session
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # 随机生成
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) # 配置7天有效

@app.route('/set')
def set_session():
    session['username'] = 'jerry'
    session['admin'] = 'tom'
    session.permanent = True # 长期有效， 一个月的时间有效
    return 'success'

@app.route('/get')
def get_session():
    username = session.get('username')
    return username

@app.route('/delete')
def delete_session():
    print(f"删除前:{session.get('username')}")
    session.pop('username')

    print(f"删除后:{session.get('username')}")
    return 'success'


@app.route('/clear')
def clear_session():
    session.clear()
    print(f"删除后:{session}")
    return 'success'

if __name__ == '__main__':
    app.run()