from flask import Flask, flash, get_flashed_messages

app = Flask(__name__)

app.secret_key = 'jerry'

@app.route('/login')
def login():
    flash('welcome to back!', category='login')
    flash('admin', category='user')
    return {'msg': 'ok'}

@app.route('/get')
def get():
    msg = get_flashed_messages(with_categories=True, category_filter=['login'])
    return {'msg': msg}

if __name__ == '__main__':
    app.run(debug=True)