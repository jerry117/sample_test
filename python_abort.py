from flask import Flask, request, abort, Response
import pprint
import werkzeug

app = Flask(__name__)

@app.route("/demo", methods=["GET"])
def demo():
    if not request.args.get('user'):
        abort(400)  # 400 bad request
    else:
        res = Response('hello world')
        return abort(res)


if __name__ == '__main__':
    pprint.pprint(werkzeug.exceptions.default_exceptions) #异常列表
    app.run(debug=True)