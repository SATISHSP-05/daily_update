from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='Pending')
    date_created = db.Column(db.DateTime, default=datetime.now)


with app.app_context():
    db.create_all()




@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        new_task = Todo(task_name=content)
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    
    tasks = Todo.query.order_by(Todo.date_created.asc()).all()
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.task_name = request.form['content']
        db.session.commit()
        return redirect('/')
    return render_template('update.html', task=task)



@app.route('/delete_all')
def delete_all():
    try:

        db.session.query(Todo).delete()
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting all tasks'
  

if __name__ == "__main__":
    app.run(debug=True)

