import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1001",
    database="pysql_db"
)

mycursor = mydb.cursor()


mycursor.execute("drop table if exists customers")

create_query = """
create table customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) not null,
    address varchar(255),
    email varchar(255) unique
)
"""

mycursor.execute(create_query)
mydb.commit()
print("Table 'customers' created successfully with id, name, address, email.")
mycursor.execute("show tables")
for table in mycursor:
    print("Table found:", table)