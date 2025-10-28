import mysql.connector
# perform LEFT JOIN to include all customers even if there's no matching employee
conn = mysql.connector.connect(host="localhost", user="root", password="1001", database="pysql_db")
cur = conn.cursor()
left_sql = (
    "SELECT customers.name AS customer_name, "
    "employee.name AS employee_name, "
    "customers.address AS customer_address, "
    "employee.address AS employee_address "
    "FROM customers "
    "LEFT JOIN employee ON customers.id = employee.id"
)
cur.execute(left_sql)
rows = cur.fetchall()
for customer_name, employee_name, customer_address, employee_address in rows:
    print("Customer Name:", customer_name)
    print("Employee Name:", employee_name if employee_name is not None else "NULL")
    print("Customer Address:", customer_address)
    print("Employee Address:", employee_address if employee_address is not None else "NULL")
    print("-----------------------------")
conn.close()