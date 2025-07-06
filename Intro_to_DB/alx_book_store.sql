-- Create Database
CREATE DATABASE IF NOT EXISTS alx_book_store;


USE alx_book_store;

-- Stores information about authors.
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);


-- tores information about books available in the bookstore.
CREATE TABLE IF NOT EXISTS BOOKS(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY(author_id) REFERENCES Authors(author_id)
   
);

-- Stores information about customers.
CREATE TABLE IF NOT EXISTS Customers(
    customer_id  INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

-- Stores information about orders placed by customers.
CREATE TABLE IF NOT EXISTS Orders(
    order_id  INT AUTO_INCREMENT PRIMARY KEY,
    customer_id  INT,
    order_date DATE NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
    
);

-- Stores information about the books included in each order.
CREATE TABLE IF NOT EXISTS Order_Details(
    orderdetailid INT  AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    order_id INT,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY(order_id) REFERENCES Orders(order_id),
    FOREIGN KEY(book_id) REFERENCES BOOKS(book_id)
    
);