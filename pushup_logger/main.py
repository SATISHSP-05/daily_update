from flask import Blueprint, render_template, session

main_bp = Blueprint("main", __name__)

# Fake product data (in real projects use a database)
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 59999, "description": "Powerful laptop for everyday use."},
    {"id": 2, "name": "Smartphone", "price": 29999, "description": "Feature-rich smartphone with great camera."},
    {"id": 3, "name": "Headphones", "price": 2999, "description": "Noise-cancelling over-ear headphones."},
    {"id": 4, "name": "Smartwatch", "price": 9999, "description": "Track your fitness and notifications."},
]


@main_bp.route("/")
def index():
    user = session.get("user")   # {'username': ..., 'full_name': ..., 'email': ...}
    return render_template("index.html", products=PRODUCTS, user=user)
