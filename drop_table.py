import mysql.connector

mydb = None
def drop_table(db_config, table_name):
    global mydb
    try:
        mydb = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        if table_name not in tables:
            print(f"Table '{table_name}' does not exist.")
            return None
        drop_table_query = f"DROP TABLE IF EXISTS {table_name}"
        cursor.execute(drop_table_query)
        mydb.commit()
        print(f"Table '{table_name}' dropped successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if mydb:
            mydb.close()
# Example usage
if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '1001',
        'database': 'pysql_db'
    }
    table_name = 'employee'
    drop_table(db_config, table_name)