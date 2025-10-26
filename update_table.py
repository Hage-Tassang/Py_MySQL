import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1001",
  database="pysql_db"
)

mycursor = mydb.cursor()

sql = "UPDATE employee SET address = 'Canyon 123' WHERE email = 'bob@example.com'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

#common practices to prevent SQL injection
# Use parameterized queries
sql = "UPDATE employee SET address = %s WHERE email = %s"
val = ('345', "alice@example.com") 

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")