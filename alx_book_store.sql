CREATE DATABASE IF NOT EXISTS alx_book_store;

--make database
use alx_book_store;

--create the books table schema
CREATE TABLE Books (
    book_id PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    FOREIGN KEY(author_id) REFERENCES Authors(author_id),
    price DOUBLE,
    publication_date DATE
);

--create Authors table schema
CREATE TABLE Authors (
    author_id PRIMARY KEY,
    author_name VARCHAR(215)
);

--create Customers table schema
CREATE TABLE Customers (
    customer_id PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215)
    address TEXT
);

--create Orders table schema
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    order_date DATE
);

--create Order_Details schema
CREATE TABLE Order_Details(
    orderdetailid PRIMARY KEY,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    book_id INT,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    quantity DOUBLE
);

