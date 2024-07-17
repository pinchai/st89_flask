from flask import Flask, render_template, request
from sqlalchemy import create_engine, text


app = Flask(__name__)

engine = create_engine("mysql+mysqlconnector://root:mysql@127.0.0.1/st89_pos")
# Test the connection
connection = engine.connect()
result = connection.execute(text("SELECT * FROM user"))
# for user in result:
#     print(f"{user[0]} - {user[1]} - {user[2]} - {user[3]}")
# print(result)


import routes


if __name__ == '__main__':
    app.run()



