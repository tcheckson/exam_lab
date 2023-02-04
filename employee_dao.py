from PyQt6.QtSql import QSqlDatabase, QSqlQuery
import sys


class EmployeeDAO:

    def __init__(self):
        # Create the connection
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName("employee.sqlite")
        # Open the connection
        if not self.con.open():
            print("Unable to connect to the database.")
            sys.exit(1)
        else:
            print("Connection successful to the database.")
            # Create a query and execute it right away using .exec()
            createTableQuery = QSqlQuery()
            createTableQuery.exec(
                """
                CREATE TABLE employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    age INTEGER NOT NULL,
                    phone INTEGER NOT NULL
                )
                """
            )

    def createEmployee(self, employee):
        if self.con.open():
            query = QSqlQuery()
            query.exec(
                f"""
                INSERT INTO employees (name, age, phone)
                VALUES ('{employee.name}', '{employee.age}', '{employee.phone}')
                """
            )
            self.con.close()
            return True
        else:
            return False

    def updateEmployee(self, employee):
        if self.con.open():
            query = QSqlQuery()
            query.exec(
                f"""
                UPADTE employees SET name='{employee.name}', age='{employee.age}', phone='{employee.phone}' WHERE id={employee.id}
                """
            )
            self.con.close()
            return True
        else:
            return False

    def deleteEmployee(self, id: int):
        if self.con.open():
            query = QSqlQuery()
            query.exec(
                f"""
                DELETE FROM employees WHERE id={id}
                """
            )
            self.con.close()
            return True
        else:
            return False

    def getEmployeeByID(self, id: int):
        data = {
            'Name': [],
            'Age': [],
            'Phone': []
        }
        if self.con.open():
            # Create and execute a query
            query = QSqlQuery()
            query.exec(f"""SELECT name, age, phone FROM employees WHERE id={id}""")
            while query.next():
                data.get('Name').append(query.value('name'))
                data.get('Age').append(str(query.value('age')))
                data.get('Phone').append(str(query.value('phone')))

            # Finish the query object if unneeded
            query.finish()
            self.con.close()

        return data

    def getAllEmployees(self):
        data = {
            'Name': [],
            'Age': [],
            'Phone': []
        }
        if self.con.open():
            # Create and execute a query
            query = QSqlQuery()
            query.exec("SELECT name, age, phone FROM employees")
            while query.next():
                data.get('Name').append(query.value('name'))
                data.get('Age').append(str(query.value('age')))
                data.get('Phone').append(str(query.value('phone')))

            # Finish the query object if unneeded
            query.finish()
            self.con.close()

        return data
