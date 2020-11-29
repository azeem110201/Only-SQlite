import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees  (
            first text,
            last text,
            pay integer
            )""")

print("table created")