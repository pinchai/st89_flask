from flask import Flask, render_template, request, redirect, json, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


@app.get('/login')
def login():
    # data = generate_password_hash('123456')
    # verify = check_password_hash(data, '123456')
    # return [data, verify]
    return render_template('auth/login.html')


@app.post('/do_login')
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == '123':
        session['is_login'] = True
        return 'login success'
    else:
        return redirect('/login')
        # data = generate_password_hash('123456')
        # verify = check_password_hash(data, '123456')
        # return [data, verify]

import routes


if __name__ == '__main__':
    app.run()



