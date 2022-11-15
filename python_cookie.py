from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/set')
def set_cookie():
    resp = make_response({'msg':'success'})
    resp.set_cookie('username', 'jerry', max_age=24*60*60)
    resp.set_cookie('admin', 'tom', max_age=24*60*60)
    return resp

@app.route('/get')
def get_cookie():
    cookie1 = request.cookies.get('username')
    return cookie1

@app.route('/delete')
def delete_cookie():
    resp = make_response({'msg':'success'})
    resp.delete_cookie('username')
    return resp

if __name__ == '__main__':
    app.run(debug=True)