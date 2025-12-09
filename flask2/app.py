# from  flask import Flask, render_template


# app = Flask('__name__')

# @app.route('/')
# def index ():
#     return render_template("home.html")

# if __name__ == "__main__":
#     app.run()


from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "change_this_secret_key"

# SQLite DB
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, "blog.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ------------------------------
# MODEL
# ------------------------------
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# Create tables
with app.app_context():
    db.create_all()


# ------------------------------
# ROUTES (CRUD)
# ------------------------------

# READ: list all posts
@app.route("/")
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("index.html", posts=posts)


# CREATE: show form + handle submit
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        if not title or not content:
            flash("Title and content are required!", "danger")
            return redirect(url_for("create"))

        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        flash("Post created successfully!", "success")
        return redirect(url_for("index"))

    return render_template("create.html")


# READ: single post
@app.route("/post/<int:post_id>")
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("detail.html", post=post)


# UPDATE: edit a post
@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
def edit(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == "POST":
        post.title = request.form.get("title")
        post.content = request.form.get("content")

        if not post.title or not post.content:
            flash("Title and content are required!", "danger")
            return redirect(url_for("edit", post_id=post_id))

        db.session.commit()
        flash("Post updated successfully!", "success")
        return redirect(url_for("detail", post_id=post.id))

    return render_template("edit.html", post=post)


# DELETE: delete a post
@app.route("/post/<int:post_id>/delete", methods=["POST"])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully!", "info")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
