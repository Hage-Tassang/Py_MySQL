import mysql.connector

mydb = None
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1001",
        database="pysql_db"
    )

'''
if mydb.is_connected():
    #print("Database connection successful!")
    # #print("Connection details:", mydb)
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name,address,email) VALUES (%s, %s, %s)"
    val = ("tassang","arunachal pradesh","hage@321")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
else:
    print("Failed to establish database connection.")
 '''


'''
if mydb.is_connected():
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name,address,email) VALUES (%s, %s, %s)"
    val = [
        ("Alice", "Wonderland", "alice@example.com"),
        ("Bob", "Builder Street", "bob@example.com"),
        ("Carol", "123 Maple Rd", "carol@example.com")
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "records inserted.")
'''
#insert multiple values
if mydb.is_connected():
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name,address,email) VALUES (%s, %s, %s)"
    val = ("David", "456 Oak St", "hgsd@gmail")
    mycursor.execute(sql, val)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)