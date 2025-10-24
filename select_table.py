import mysql.connector

mydb = None
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1001",
        database="pysql_db"
    )

#query object 
mycursor = mydb.cursor()


# print("\n-----fetchall() example-----")
# # query to select all records from customers table
# mycursor.execute("SELECT * FROM customers")
# #Note: We use the fetchall() method, which fetches all rows from the last executed statement.
# # fetch all results from executed query
# myres = mycursor.fetchall()

# for record in myres:
#     print(record)


# print("\n-----fetchone() example-----")
# mycursor.execute("SELECT * FROM customers")
# record1 = mycursor.fetchone()
# print(record1)

# print("\n-----fetchone()at a time example-----")
# #using fetchone() method to get one record at a time
# mycursor.execute("SELECT * FROM customers")
# while True:
#     record = mycursor.fetchone()
#     if record is None:
#         break
#     print(record)


print("\n-----select specific columns-----")
#selecting specific columns
mycursor.execute("SELECT address, email FROM customers")
my_res1 = mycursor.fetchall()
for record in my_res1:
    print(record)


mydb.close()