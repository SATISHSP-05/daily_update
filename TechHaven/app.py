from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = 'your_secret_key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Niki123' 
app.config['MYSQL_DB'] = 'ecommerce_db'

mysql = MySQL(app)


def get_cart_count():
    return len(session.get('cart', []))


@app.context_processor
def inject_cart_count():
    return dict(cart_count=get_cart_count())

# routes

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

# Cart Routes

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    
    # Prevent duplicate items for simplicity
    if product_id not in session['cart']:
        session['cart'].append(product_id)
        session.modified = True
        flash('Item added to cart!', 'success')
    else:
        flash('Item is already in your cart.', 'info')
        
    return redirect(request.referrer or url_for('home'))

@app.route('/cart')
def cart():
    if 'cart' not in session or not session['cart']:
        return render_template('cart.html', products=[], total=0)
    
    cart_ids = session['cart']
    # Create a placeholder string for the SQL query (e.g., "%s, %s, %s")
    placeholders = ','.join(['%s'] * len(cart_ids))
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # Fetch details for all products in the cart
    cursor.execute(f'SELECT * FROM products WHERE id IN ({placeholders})', tuple(cart_ids))
    products = cursor.fetchall()
    
    # Calculate total price
    total_price = sum(product['price'] for product in products)
    
    return render_template('cart.html', products=products, total=total_price)

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    if 'cart' in session and product_id in session['cart']:
        session['cart'].remove(product_id)
        session.modified = True
        flash('Item removed from cart.', 'warning')
    return redirect(url_for('cart'))

# Auth Routes
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
        except:
            flash('Username already exists!', 'danger')
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
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('cart', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)