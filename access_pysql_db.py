import mysql.connector

mydb = None
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1001",
        database="pysql_db"
    )
    if mydb.is_connected():

        print("Database connection successful!")
        print("Connection details:", mydb)

    else:
        print("Failed to establish database connection.")
except Error as e:
    print("An error occurred when connecting to the database:", e)