import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="6440",
)
print(conn)
cursor = conn.cursor()

db_name = "python_test_db"
query = "create database " + db_name
cursor.execute(query)