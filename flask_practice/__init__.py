# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("home.html")


# @app.route('/home')
# def home():
#     return render_template('home.html')



# @app.route('/about')
# def about():
#     return render_template('about.html')


# @app.route('/contact')
# def contact():
#     return render_template('contact.html')


# @app.route('/profile')
# def profile():
#     return render_template('profile.html')

# if __name__ == "__main__":
#     app.run()




from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ===== Simple in-memory "database" for blog posts =====
# Each post: {"id": int, "title": str, "content": str}
posts = []
next_id = 1


# ===== Existing pages =====

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


# ===== BLOG ROUTES =====

# READ (list) + CREATE (form submit)
@app.route("/blog", methods=["GET", "POST"])
def blog_list():
    global posts, next_id

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        if title and content:
            posts.append({
                "id": next_id,
                "title": title,
                "content": content
            })
            next_id += 1

        return redirect(url_for("blog_list"))

    # GET: show list + create form
    return render_template("blog_list.html", posts=posts)


# READ single
@app.route("/blog/<int:post_id>")
def blog_detail(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return "Post not found", 404
    return render_template("blog_detail.html", post=post)


# UPDATE
@app.route("/blog/<int:post_id>/edit", methods=["GET", "POST"])
def blog_edit(post_id):
    global posts
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return "Post not found", 404

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        if title and content:
            post["title"] = title
            post["content"] = content
        return redirect(url_for("blog_detail", post_id=post_id))

    return render_template("blog_edit.html", post=post)


# DELETE
@app.route("/blog/<int:post_id>/delete", methods=["POST"])
def blog_delete(post_id):
    global posts
    posts = [p for p in posts if p["id"] != post_id]
    return redirect(url_for("blog_list"))


if __name__ == "__main__":
    app.run(debug=True)
