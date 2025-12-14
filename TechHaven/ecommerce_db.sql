DROP DATABASE IF EXISTS ecommerce_db;
CREATE DATABASE ecommerce_db;
USE ecommerce_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    image_url VARCHAR(500),
    category VARCHAR(50)
);

-- Insert more products with real images
INSERT INTO products (name, price, image_url, category) VALUES
('Wireless Noise-Canceling Headphones', 249.99, 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&q=80', 'Electronics'),
('Ergonomic Gaming Mouse', 59.99, 'https://images.unsplash.com/photo-1527814050087-3793815479db?w=500&q=80', 'Gaming'),
('RGB Mechanical Keyboard', 129.50, 'https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=500&q=80', 'Gaming'),
('4K Gaming Monitor, 27-inch', 349.00, 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500&q=80', 'Electronics'),
('Smartwatch with Health Tracking', 199.50, 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&q=80', 'Wearables'),
('Minimalist Laptop Backpack', 45.00, 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500&q=80', 'Accessories'),
('Portable Bluetooth Speaker', 39.95, 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500&q=80', 'Audio'),
('Ceramic Coffee Mug Set', 25.00, 'https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=500&q=80', 'Home');