from flask import Flask, request, g

app = Flask(__name__)

def is_admin():
    if g.user == 'admin':
        return True
    else:
        return False


@app.route('/login')
def login():
    user = request.args.get('username')
    g.user = user
    if is_admin():
        return {'msg': 'ok', 'admin': 'yes'}
    else:
        return {'msg': 'ok', 'admin': 'no'}

if __name__ == '__main__':
    app.run(debug=True)

