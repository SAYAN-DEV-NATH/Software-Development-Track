import mysql.connector

db_name = "python_test_db"
conn = mysql.connector.connect(
    host="localhost", user="root", password="6440", database=db_name
)
cursor = conn.cursor()

query = """
        update student
        set name = "KKR"
        where roll = '101'
        """

cursor.execute(query)
conn.commit()
print("Create table successfun")
