from app import app, render_template, request, redirect
from sqlalchemy import create_engine, text

engine = create_engine("mysql+mysqlconnector://root:@127.0.0.1/st89_pos")
# Test the connection
connection = engine.connect()


@app.route('/crud')
def crud():
    result = connection.execute(text("SELECT * FROM user"))
    connection.commit()
    return render_template('crud.html', data=result)


@app.post('/create')
def create():
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    address = request.form.get('address')
    result = connection.execute(text(f"INSERT INTO `user` VALUES(null, '{name}', '{gender}', '{address}')"))
    connection.commit()
    return redirect('/crud')


@app.get('/confirm_delete')
def confirm_delete():
    user_id = request.args.get('id')
    result = connection.execute(text(f"select * from user where id={user_id}"))
    connection.commit()
    data = []
    for user in result:
        data.append({
            'id': user[0],
            'name': user[1],
            'gender': user[2],
            'address': user[3],
        })
    return render_template('confirm_delete.html', data=data)


@app.get('/delete_user')
def delete_user():
    user_id = request.args.get('id')
    result = connection.execute(text(f"DELETE FROM `user` WHERE id = {user_id}"))
    connection.commit()
    return redirect('/delete')


@app.route('/delete')
def delete():
    result = connection.execute(text("SELECT * FROM user"))
    connection.commit()
    return render_template('crud.html', data=result)
