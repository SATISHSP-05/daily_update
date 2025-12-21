from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response, jsonify
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, set_access_cookies, unset_jwt_cookies, verify_jwt_in_request
import MySQLdb.cursors
from datetime import timedelta  

app = Flask(__name__)

# --- Configuration ---
app.secret_key = 'your_secret_key'  
app.config['JWT_SECRET_KEY'] = 'super-secret-jwt-key'  
app.config['JWT_TOKEN_LOCATION'] = ['cookies']         
app.config['JWT_COOKIE_CSRF_PROTECT'] = False          
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1) 

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Niki123' 
app.config['MYSQL_DB'] = 'ecommerce_db'

mysql = MySQL(app)
jwt = JWTManager(app)

#  Handle Expired/Missing Tokens
@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    resp = make_response(redirect(url_for('login')))
    unset_jwt_cookies(resp)
    flash('Your session has expired. Please login again.', 'warning')
    return resp

@jwt.unauthorized_loader
def my_unauthorized_callback(reason):
    flash('You must be logged in to view that page.', 'warning')
    return redirect(url_for('login'))

# ] Helper: Check Login Status for Templates]
def is_logged_in():
    try:
        verify_jwt_in_request(optional=True)
        if get_jwt_identity():
            return True
    except:
        return False
    return False

@app.context_processor
def inject_globals():
    logged_in = is_logged_in()
    current_user = get_jwt_identity() if logged_in else None
    cart_count = len(session.get('cart', []))
    return dict(logged_in=logged_in, current_user=current_user, cart_count=cart_count)

# Routes 

@app.route('/')
def home():
    search_query = request.args.get('q')
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    if search_query:
        query_string = "%" + search_query + "%"
        cursor.execute('SELECT * FROM products WHERE name LIKE %s', (query_string,))
    else:
        cursor.execute('SELECT * FROM products')
        
    products = cursor.fetchall()
    return render_template('index.html', products=products, search_query=search_query)

# --- Cart Routes ---

@app.route('/add_to_cart/<int:product_id>')
@jwt_required()  
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    
    if product_id not in session['cart']:
        session['cart'].append(product_id)
        session.modified = True
        flash('Item added to cart!', 'success')
    else:
        flash('Item is already in your cart.', 'info')
        
    return redirect(request.referrer or url_for('home'))

@app.route('/cart')
@jwt_required() 
def cart():
    if 'cart' not in session or not session['cart']:
        return render_template('cart.html', products=[], total=0)
    
    cart_ids = session['cart']
    if not cart_ids:
         return render_template('cart.html', products=[], total=0)

    placeholders = ','.join(['%s'] * len(cart_ids))
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f'SELECT * FROM products WHERE id IN ({placeholders})', tuple(cart_ids))
    products = cursor.fetchall()
    
    total_price = sum(product['price'] for product in products)
    return render_template('cart.html', products=products, total=total_price)

@app.route('/remove_from_cart/<int:product_id>')
@jwt_required() 
def remove_from_cart(product_id):
    if 'cart' in session and product_id in session['cart']:
        session['cart'].remove(product_id)
        session.modified = True
        flash('Item removed from cart.', 'warning')
    return redirect(url_for('cart'))

# --- Auth Routes ---

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_pw = generate_password_hash(password)

        cursor = mysql.connection.cursor()
        try:
            cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)', (username, email, hashed_pw))
            mysql.connection.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('Username or Email already exists!', 'danger')
            
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()

        if account and check_password_hash(account['password'], password):
            access_token = create_access_token(identity=username)
            
            print("JWT TOKEN:", access_token) 
            resp = make_response(redirect(url_for('home')))
            set_access_cookies(resp, access_token)
            flash('Logged in successfully!', 'success')
            return resp
        else:
            flash('Incorrect username or password', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('login')))
    unset_jwt_cookies(resp)
    session.pop('cart', None) 
    flash('You have been logged out.', 'info')
    return resp

if __name__ == '__main__':
    app.run(debug=True)