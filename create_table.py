import mysql.connector
from mysql.connector import Error

mydb = None
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1001",
        database="pysql_db"
    )
    if mydb.is_connected():

        print("Database connection successful!")
        print("Connection details:", mydb)
        print("creating table in pysql_db...")

        #create a cursor object to execute SQL queries

        
        mycursor = mydb.cursor()
        #mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
        print("Table 'customers' created successfully.")

        #common constrains: PRIMARY KEY, AUTO_INCREMENT, NOT NULL, UNIQUE
        #adding constraints example
        #mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR
        #(255) NOT NULL, address VARCHAR(255) UNIQUE)")
        
        #mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
        #print("Table 'customers' created successfully.")
        
        #If the table already exists, use the ALTER TABLE keyword:
        mycursor.execute("DROP TABLE IF EXISTS customers")
        print("Dropped existing 'customers' table (if any).")

        create_query = """
        CREATE TABLE customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255),
            email VARCHAR(255) UNIQUE
        )
        """
        mycursor.execute(create_query)
        mydb.commit()
        print("Created new 'customers' table with id, name, address, email.")
        #mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
        #mycursor.execute("ALTER TABLE customers ADD COLUMN email VARCHAR(255)")
        print("Column 'email' added to 'customers' table.")
        
        #check if table is created
        mycursor.execute("SHOW TABLES")
        for table in mycursor:
            print("Table found:", table)

        

    else:
        print("Failed to establish database connection.")
except Error as e:
    print("An error occurred when connecting to the database:", e)