from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    student_list = [
        {
            'id': 'st001',
            'name': 'vuthy',
            'gender': 'male',
            'profile': 'sara.jpeg',
        },
        {
            'id': 'st002',
            'name': 'dara',
            'gender': 'male',
            'profile': 'sara.jpeg',
        },
        {
            'id': 'st001',
            'name': 'vuthy',
            'gender': 'male',
            'profile': 'sara.jpeg',
        },
        {
            'id': 'st002',
            'name': 'dara',
            'gender': 'male',
            'profile': 'sara.jpeg',
        },
    ]
    age = 100
    return render_template('home.html', student_list=student_list)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run()
