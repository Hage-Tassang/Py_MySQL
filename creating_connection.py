#import necessary modules
import mysql.connector

#set up database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1001",
    database="test0"
)

#print("Database connection successful!")
print("Connection details:", mydb)

mydb.close()

print("Database connection closed.")