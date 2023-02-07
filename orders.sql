DROP TABLE orders;

CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    customer_name VARCHAR(30) NOT NULL,
    drink_type VARCHAR(50) NOT NULL, 
    drink_size VARCHAR(20) NOT NULL,
    extras VARCHAR(50) NOT NULL,
    price NUMERIC NOT NULL 
);

INSERT INTO orders (customer_name, drink_type, drink_size, extras, price) VALUES ('Charlie', 'Latte', 'Large', 'Chocolate srpinkles', 3.85);
INSERT INTO orders (customer_name, drink_type, drink_size, extras, price) VALUES ('Craig', 'Mocha', 'Large', 'Sugar', 3.50);
INSERT INTO orders (customer_name, drink_type, drink_size, extras, price) VALUES ('Louise', 'Hot Chocolate', 'Medium', 'Cream', 3.25);
