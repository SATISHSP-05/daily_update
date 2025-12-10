from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint("auth", __name__)

# Fake user "database"
# USERS[username] = {"password": "...", "full_name": "...", "email": "..."}
USERS = {}


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        print(full_name, username, email, password)

        if not (full_name and username and email and password and confirm_password):
            flash("All fields are required.", "error")
            return redirect(url_for("auth.signup"))

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for("auth.signup"))

        if username in USERS:
            flash("Username already exists. Try another one.", "error")
            return redirect(url_for("auth.signup"))

        USERS[username] = {
            "full_name": full_name,
            "email": email,
            "password": password,
        }

        flash("Signup successful! Please login.", "success")
        return redirect(url_for("auth.login"))
    
    
    return render_template("signup.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = USERS.get(username)

        if not user or user["password"] != password:
            flash("Invalid username or password.", "error")
            return redirect(url_for("auth.login"))

        # Save minimal info in session
        session["user"] = {
            "username": username,
            "full_name": user["full_name"],
            "email": user["email"],
        }

        flash("Logged in successfully!", "success")
        return redirect(url_for("main.index"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("main.index"))


@auth_bp.route("/profile")
def profile():
    user = session.get("user")
    if not user:
        flash("Please login to see your profile.", "error")
        return redirect(url_for("auth.login"))

    return render_template("profile.html", user=user)
