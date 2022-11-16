from flask import Flask, current_app

# 在flask内部维护者两个线程隔离的栈，current_app指向了AppContext(应用上下文)中的栈顶，request指向了RequestContext(请求上下文)栈顶

app = Flask(__name__)
print(f'app object name: {app}, object id:{id(app)}')

print(app)
with app.app_context():
    app2 = current_app
    print(app2)

@app.route('/demo')
def demo():
    print(current_app)
    return {'msg': 'ok'}

if __name__ == '__main__':
    app.run()