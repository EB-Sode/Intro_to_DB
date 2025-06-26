import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="firstsql", database="alx_book_store")
cursor = mydb.cursor()

try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database created successfully!")
except mysql.connector.Error as e:
    print("Error occurred while creating database", e)

cursor.execute("USE alx_book_store")

schema = """



CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

CREATE TABLE IF NOT EXISTS Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
);

CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE IF NOT EXISTS Order_Details(
    orderdetailid INT PRIMARY KEY,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    book_id INT,
    quantity DOUBLE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
"""

with open("task_2.sql", "w") as file:
    file.write(schema)

# cursor.execute("SHOW TABLES")
# result = cursor.fetchall()
# result = "\n".join([f"Table: {table[0]}" for table in result])



with open("task_3.sql", "w") as f:
    f.write("SHOW TABLES;")
