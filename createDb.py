#import necessary modules
import mysql.connector
from mysql.connector import Error

# set up database connection with simple exception handling
mydb = None
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1001",
    )
    if mydb.is_connected():

        print("Database connection successful!")
        print("Connection details:", mydb)

    else:
        print("Failed to establish database connection.")
except Error as e:
    print("An error occurred when connecting to the database:", e)
#finally:
    #if mydb and mydb.is_connected():
        #mydb.close()
        #print("Database connection closed.")

mycursor = None
if mydb.is_connected():
    mycursor = mydb.cursor()
    #to create a new database uncomment the following line

    mycursor.execute("CREATE DATABASE psql_db2")
    if mycursor:
        mycursor.execute("SHOW DATABASES")
        for db in mycursor:
            print("Database found:", db)

mydb.close()
print("Database connection closed.")