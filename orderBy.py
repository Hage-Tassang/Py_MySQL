import mysql.connector
from mysql.connector import Error
mydb = None
query_data = None
try:
    mydb =  mysql.connector.connect(
    host= "localhost",
    user="root",
    password="1001",
    database="pysql_db"
    )
    
except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)

finally:
    try:
        if mydb.is_connected():
            #fetching the database server information
            db_Info = mydb.get_server_info()
            print("Connected to MySQL Server version ", db_Info)

        if mydb is not None:

            #cursor object also used to execute the queries also fetch the results
            mycursor = mydb.cursor()

            #query statement to fetch all the records from the table customers ordered by name
            
            #ascending order
            #sql_orderby_query = "SELECT * FROM Customers ORDER BY name"

            #descending order
            sql_orderby_query = "SELECT * FROM Customers ORDER BY name desc"

            #execute the query
            result = mycursor.execute(sql_orderby_query)
            #fetch all the records from the 'cursor' object
            print("\nPrinting the records in descending order")
            print("=====================================")
            print("ID\tName\tAddress")
            print("--\t----\t-------")
            print("\n")
            query_data = mycursor.fetchall()
            for row in query_data:
                print("{}\t{}\t{}".format(row[0], row[1], row[2]))

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)

