from flask import Flask, render_template, request
import requests
from datetime import date

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    student_list = []

    arr = [1,2,3]
    print(arr[5])

    res = requests.get('https://fakestoreapi.com/products')
    res_json = res.json()
    return render_template('home.html', product_list=res_json)


@app.get('/shop_now')
def shopNow():
    id = request.args.get('id')
    res = requests.get(f"https://fakestoreapi.com/products/{id}")
    json = res.json()
    return render_template('shop_now.html', product=json)


@app.get('/checkout')
def checkout():
    id = request.args.get('id')
    res = requests.get(f"https://fakestoreapi.com/products/{id}")
    json = res.json()
    return render_template('checkout.html', product=json)


@app.post('/confirmBooking')
def confirmBooking():
    product_id = request.form.get('product_id')
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')
    res = requests.get(f"https://fakestoreapi.com/products/{product_id}")
    product = res.json()

    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    msg = (
        "<strong>New Confirm Booking 🛎️</strong>\n"
        "<code>Name: {name}</code>\n"
        "<code>Phone: {phone}</code>\n"
        "<code>Email: {email}</code>\n"
        "<code>Address: {address}</code>\n"
        "<code>Booking Date: {date}</code>\n"
        "<code>=======================</code>\n"
        "<code>1. {product_name} 1x{price}</code>\n"
    ).format(
        name=name,
        phone=phone,
        email=email,
        address=address,
        date=date.today(),
        product_name=product['title'],
        price=product['price']
    )
    notify_res = sendNotify(msg)
    return notify_res.json()


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.post('/submit_contact')
def submitContact():
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    msg = (
        "<strong>New Notification</strong>\n"
        "<code>Customer Name: {name}</code>\n"
        "<code>Customer Email: {email}</code>\n"
        "<code>Customer Address: {address}</code>\n"
        "<code>📆 {date}</code>\n"
    ).format(
        name=name,
        email=email,
        address=address,
        date=date.today(),
    )
    sendNotify(msg)

    return 'work'


@app.errorhandler(404)
def error404(e):
    return render_template('/error/404.html')


@app.errorhandler(500)
def error404(e):
    return render_template('/error/500.html')


if __name__ == '__main__':
    app.run()


def sendNotify(msg):
    bot_token = "6986363245:AAEKpwak_fBiBX9Pmy08IyxjuH1-_zf0Dqo"
    chat_id = "@st89_channel"

    html = msg

    html = requests.utils.quote(html)
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={html}&parse_mode=HTML"
    res = requests.get(url)
    return res
