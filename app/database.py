import sqlite3

DATABASE = "employees.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT NOT NULL,
            salary REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def get_all_employees():
    connection = get_connection()

    employees = connection.execute(
        "SELECT * FROM employees ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return employees


def add_employee(name, department, email, salary):
    connection = get_connection()

    connection.execute(
        """
        INSERT INTO employees
        (name, department, email, salary)
        VALUES (?, ?, ?, ?)
        """,
        (name, department, email, salary)
    )

    connection.commit()
    connection.close()


def delete_employee(employee_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )

    connection.commit()
    connection.close()