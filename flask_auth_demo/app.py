# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from models import db, User
import datetime

app = Flask(__name__)

# ====== Config ======
app.config["SECRET_KEY"] = "change_this_secret"  # for Flask-Login / sessions
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "change_this_jwt_secret"  # for JWT tokens

# ====== Extensions init ======
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"  # redirect to login when @login_required fails
login_manager.init_app(app)

jwt = JWTManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Runs once at startup
with app.app_context():
    db.create_all()


#       HTML ROUTES

@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Username and password required", "danger")
            return redirect(url_for("register"))

        if User.query.filter_by(username=username).first():
            flash("Username already exists", "danger")
            return redirect(url_for("register"))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.", "info")
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", username=current_user.username)


#      API (JWT) ROUTES

@app.route("/api/login", methods=["POST"])
def api_login():
    """
    Accept JSON: { "username": "", "password": "" }
    Returns: { "access_token": "..." }
    """
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Missing JSON body"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "username and password required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"msg": "Bad username or password"}), 401

    # token expires in 30 minutes
    expires = datetime.timedelta(minutes=30)
    access_token = create_access_token(identity=user.id, expires_delta=expires)

    return jsonify(access_token=access_token), 200


@app.route("/api/protected", methods=["GET"])
@jwt_required()
def protected_api():
    """
    Requires JWT token in Authorization header:
    Authorization: Bearer <token>
    """
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify(
        {
            "msg": "Hello from protected API!",
            "user_id": current_user_id,
            "username": user.username if user else None,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
