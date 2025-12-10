from flask import Flask
from auth import auth_bp
from main import main_bp   # ✅ FIX IS HERE

app = Flask(__name__)
app.secret_key = "ecommerce_secret_key"

app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(debug=True)
