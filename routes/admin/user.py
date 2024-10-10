from app import app, render_template, request
from sqlalchemy import create_engine, text

engine = create_engine("mysql+mysqlconnector://root:mysql@127.0.0.1/st89_pos")
# Test the connection
connection = engine.connect()

@app.get('/admin/user')
def user():
    module = 'user'
    return render_template('admin/user.html', module=module)


@app.get('/admin/get-user')
def getUser():
    result = connection.execute(text("SELECT * FROM user"))
    recode = result.fetchall()
    data = []
    for item in recode:
        data.append(
            {
                'id': item[0],
                'name': item[1],
                'gender': item[2],
                'phone': '099 888 777',
                'address': item[3],
            }
        )
    connection.commit()
    return data


@app.post('/admin/create-user')
def createUser():
    form_date = request.get_json()
    name = form_date['name']
    gender = form_date['gender']
    phone = form_date['phone']
    email = form_date['email']
    address = form_date['address']
    password = form_date['password']

    result = connection.execute(text(f"INSERT INTO `user` VALUES (NULL,'{name}','{gender}','{password}','{phone}','{email}','{address}')"))
    connection.commit()
    return [name, gender, phone, email, address, password]



