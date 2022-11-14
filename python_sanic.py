from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

@app.route('/')
async def index(request):
    return json({'code':200, 'message':'success', 'data': request.args})


@app.get('/get')
async def index(request):
    return json({'code':200, 'message':'success', 'data': request.args})

@app.route('/test/<u_id>')
async def test(request, u_id):
    return json({'code':200, 'message':'success', 'data': u_id})

@app.route("/test")
async def test1(request):
    return json({'url': request.url})

if __name__ == '__main__':
    app.run(debug=True)