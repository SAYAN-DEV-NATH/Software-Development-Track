import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="6440",
    database="dummydb"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM employees")

result = cursor.fetchall()
for row in result:
    print(row)

conn.close()