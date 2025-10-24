import mysql.connector

mydb = None
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1001",
        database="pysql_db"
    )

mycursor = mydb.cursor()
id = 3
sql_where_query = "SELECT * FROM Customers WHERE ID = {}".format(id)
mycursor.execute(sql_where_query)

myresult = mycursor.fetchall()

for row in myresult:
    print(row)

sql = "SELECT * FROM customers WHERE address LIKE '%c%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)