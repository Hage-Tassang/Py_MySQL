import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1001",
        database="pysql_db"
    )

    mycursor = mydb.cursor()
    sql = "SELECT * FROM employee LIMIT %s offset 2" #to start from another position u can use offset clause
    limit_value = (5,)  # Limit to 5 results
    mycursor.execute(sql, limit_value)
    results = mycursor.fetchall()
    for row in results:
        print(row)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()