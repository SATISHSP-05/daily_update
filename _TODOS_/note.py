
@app.route('/api/tasks', methods=['GET', 'POST'])
def api_tasks():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'task' not in data:
            return jsonify({"error": "Missing 'task' key"}), 400
        new_task = Todo(task_name=data['task'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Task created", "id": new_task.id}), 201

    tasks = Todo.query.all()
    output = []
    for t in tasks:
        output.append({'id': t.id, 'task': t.task_name, 'date': t.date_created.strftime('%Y-%m-%d %H:%M')})
    return jsonify(output)

@app.route('/api/tasks/<int:id>', methods=['PUT', 'DELETE'])
def api_task_detail(id):
    task = Todo.query.get_or_404(id)
    
    if request.method == 'PUT':
        data = request.get_json()
        task.task_name = data.get('task', task.task_name)
        db.session.commit()
        return jsonify({"message": "Updated"})

    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Deleted"})

@app.route('/api/tasks/delete_all', methods=['DELETE'])
def api_delete_all():
    db.session.query(Todo).delete()
    db.session.commit()
    return jsonify({"message": "All tasks cleared"})





from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# 1. Database Configuration
# This creates a local file named 'todo.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

 # 2. Data Model (The 'Table' structure)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='Pending')
    date_created = db.Column(db.DateTime, default=datetime.now)

# Initialize Database
with app.app_context():
    db.create_all()

# --- CRUD ROUTES ---

# READ & CREATE
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

# DELETE
@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

# UPDATE
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.task_name = request.form['content']
        db.session.commit()
        return redirect('/')
    return render_template('update.html', task=task)



# Add this route to your app.py
@app.route('/delete_all')
def delete_all():
    try:
        # This deletes every record in the Todo table
        db.session.query(Todo).delete()
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting all tasks'
  

if __name__ == "__main__":
    app.run(debug=True)

