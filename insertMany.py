import mysql.connector

mydb = None
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1001",
        database="pysql_db"
    )

mycursor = mydb.cursor()

sql = "insert into customers (name, address) VALUES (%s, %s)"

val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]


#insert multiple records using executemany()
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

mydb.close()

# reopen the existing connection if it's closed, then drop the column
if not mydb.is_connected():
    mydb.reconnect(attempts=3, delay=2)

mycursor = mydb.cursor()
try:
    mycursor.execute("ALTER TABLE customers DROP COLUMN email")
    mydb.commit()
    print("Column 'email' dropped from customers.")
except mysql.connector.Error as e:
    print("Failed to drop column 'email':", e)
finally:
    mycursor.close()
    mydb.close()