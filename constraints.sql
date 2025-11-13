ALTER TABLE Customers 
ADD CONSTRAINT unique_customer_name 
UNIQUE (first_name, last_name);

ALTER TABLE Orders 
ADD CONSTRAINT fk_order_customer 
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE;

ALTER TABLE Orders 
ADD CONSTRAINT check_amount_positive CHECK (amount >= 100);

ALTER TABLE Shippings 
ADD CONSTRAINT fk_shipping_customer 
FOREIGN KEY (customer) REFERENCES Customers(customer_id) ON UPDATE CASCADE;

ALTER TABLE Shippings 
ADD CONSTRAINT check_status_range 
CHECK (status BETWEEN 0 AND 5);

ALTER TABLE Customers 
ADD CONSTRAINT chk_age_limit CHECK (age BETWEEN 18 AND 100);

ALTER TABLE Orders 
ADD CONSTRAINT unique_order_item UNIQUE (item, customer_id);

ALTER TABLE Shippings 
ADD CONSTRAINT chk_shipping_status CHECK (status >= 0 AND status <= 10);

ALTER TABLE Orders 
ADD CONSTRAINT df_amount DEFAULT 500 FOR amount;



