from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return '<center><h1 style="color: red">Hello from home page</h1></center>'


@app.route('/contact')
def hello_contact():
    return '<center><h1 style="color: hotpink">Hello from contact page</h1></center>'


@app.route('/about')
def hello_about():
    return '<center><h1 style="color: DarkSeaGreen">Hello from about page</h1></center>'


if __name__ == '__main__':
    app.run()
