import mysql.connector

db_name = "python_test_db"

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="6440",
    database = db_name
)
cursor = conn.cursor()

query = """
        create table student
        (
            roll varchar(4),
            Name varchar(50)
        )
        """

cursor.execute(query)
print("Create table successfun")