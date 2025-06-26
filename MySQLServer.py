import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="firstsql")
cursor = mydb.cursor()

try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database created successfully!")
except Exception as e:
    print("Error occurred while creating database:", e)

cursor.close()
mydb.close()