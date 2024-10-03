import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="6440", database="student"
)
cursor = conn.cursor()

query = """
        create table students(
            roll int primary key,
            name varchar(20)
        );

        create table book(
            bookId int primary key,
            bookName varchar(20)
        );

        create table librarian(
            libID int primary key,
            libName varchar(20)
        );
        """

cursor.execute(query)
