from flask import Flask
from flask_mail import Mail, Message
from httpx import main

app = Flask(__name__)

# 邮箱配置
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'XXX@qq.com'
app.config['MAIL_PASSWORD'] = '**************'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# mail 实例
mail = Mail(app)


@app.route('/mail')
def send_mail():
    message = Message('hello world', sender='XXX@Gmail.com', recipients=['XXX@Gmail.com'])
    message.body = 'hello flask message sent from flask-mail'
    mail.send(message)
    return {'msg': 'send mail ok'}

if __name__ == '__main__':
    app.run(debug=True)