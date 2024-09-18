from flask import Flask, render_template, request, redirect, json, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)


import routes


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
        session['auth'] = {
            'user': username,
            'role': "admin",
        }
        return redirect('/admin')
    else:
        return redirect('/login')
        # data = generate_password_hash('123456')
        # verify = check_password_hash(data, '123456')
        # return [data, verify]


@app.route('/check_session_lifetime')
def check_session_lifetime():
    is_permanent = session.permanent
    session_lifetime = app.config['PERMANENT_SESSION_LIFETIME']
    return f"<h1>Session is permanent: {is_permanent}, Lifetime: {session_lifetime}</h1>"


@app.get('/admin')
def admin():
    if 'is_login' in session:
        return render_template('auth/admin.html', data=session["is_login"])
    return 'You are not logged in <br><a href="/login">Login</a>'


if __name__ == '__main__':
    app.run()



