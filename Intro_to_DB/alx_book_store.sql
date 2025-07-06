--Create Database
CREATE DATABASE IF NOT EXISTS alx_book_store;


USE alx_book_store;

--Stores information about authors.
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT AUTO_INCREMENT Primary Key,
    author_name VARCHAR(215) NOT NULL
);


--Stores information about books available in the bookstore.
CREATE TABLE IF NOT EXISTS BOOKS(
    book_id INT AUTO_INCREMENT Primary Key,
    title VARCHAR(130),
    Foreign Key(author_id) REFERENCES Authors (author_id),
    price DOUBLE,
    publication_date DATE
);

--Stores information about customers.
CREATE TABLE IF NOT EXISTS Customers(
    customer_id  INT AUTO_INCREMENT Primary Key,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

--Stores information about orders placed by customers.
CREATE TABLE IF NOT EXISTS Orders(
    order_id  INT AUTO_INCREMENT Primary Key,
    Foreign Key(customer_id) REFERENCES Customers(customer_id),
    order_date DATE NOT NULL
);

--Stores information about the books included in each order.
CREATE TABLE IF NOT EXISTS Order_Details(
    orderdetailid INT  AUTO_INCREMENT Primary Key,
    Foreign Key(order_id) REFERENCES Orders (order_id),
    Foreign Key(book_id) REFERENCES BOOKS (book_id),
    quantity DOUBLE NOT NULL
);