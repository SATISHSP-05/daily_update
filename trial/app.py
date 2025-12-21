# from flask import Flask, render_template, request, redirect, url_for
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Niki123'
# app.config['MYSQL_DB'] = 'flask_auth'

# mysql = MySQL(app)

# @app.route('/')
# def register():
#     return render_template('register.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route('/save', methods=['POST'])
# def register_user():
#     name = request.form['name']
#     password = request.form['password']

#     cur = mysql.connection.cursor()
#     cur.execute(
#         "INSERT INTO users (name, password) VALUES (%s, %s)",
#         (name, password)
#     )
#     mysql.connection.commit()
#     cur.close()

#     return redirect(url_for('login'))

# @app.route('/check', methods=['POST'])
# def login_user():
#     name = request.form['name']
#     password = request.form['password']

#     cur = mysql.connection.cursor()
#     cur.execute(
#         "SELECT * FROM users WHERE name=%s AND password=%s",
#         (name, password)
#     )
#     user = cur.fetchone()
#     cur.close()

#     if user:
#         return redirect(url_for('index'))
#     else:
#         return "Invalid Login"

# if __name__ == '__main__':
#     app.run(debug=True)








from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Niki123@localhost/flask_auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def register_user():
    name = request.form['name']
    password = request.form['password']

    user = User(name=name, password=password)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/check', methods=['POST'])
def login_user():
    name = request.form['name']
    password = request.form['password']

    user = User.query.filter_by(name=name, password=password).first()

    if user:
        return redirect(url_for('index'))
    else:
        return "Invalid Login"

if __name__ == '__main__':
    app.run(debug=True)
