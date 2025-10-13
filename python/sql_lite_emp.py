import sqlite3

conn = sqlite3.connect("office.db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    role TEXT,
    salary REAL
)
"""
)

print("Table created successfully!")
conn.commit()
conn.close()


conn = sqlite3.connect("office.db")
cursor = conn.cursor()

employees_data = [
    ("Ravi Sharma", 28, "Software Engineer", 60000),
    ("Priya Mehta", 32, "Project Manager", 85000),
    ("Karan Patel", 25, "Data Analyst", 50000),
    ("Neha Singh", 30, "HR Executive", 45000),
]

cursor.executemany(
    "INSERT INTO employees (name, age, role, salary) VALUES (?, ?, ?, ?)",
    employees_data,
)

conn.commit()
print("Employee records inserted successfully!")
conn.close()


conn = sqlite3.connect("office.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees WHERE salary > 50000")
print("Employees earning above 50000:")
print(cursor.fetchall())

cursor.execute("SELECT * FROM employees WHERE role = 'HR Executive'")
print("\nEmployees with role 'HR Executive':")
print(cursor.fetchall())


conn.close()
