import mysql.connector

mydb = None
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1001",
        database="pysql_db"
    )

mycursor = mydb.cursor()
sql = " SELECT \
    customers.name AS customer_name, \
    employee.name AS employee_name, \
    customers.address AS customer_address, \
    employee.address AS employee_address \
    FROM customers \
    JOIN employee on customers.id = employee.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    print("Customer Name:", row[0])
    print("Employee Name:", row[1])
    print("Customer Address:", row[2])
    print("Employee Address:", row[3])
    print("-----------------------------")
mydb.close()


