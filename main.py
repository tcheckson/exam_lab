# main_window.py
"""Main window-style application."""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableView,
)
import employee_form
import employee_dao
import table_view


class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Final Exam App")
        self.setGeometry(500, 200, 500, 400)
        self.table = QTableView()
        self.populate_table()
        self.createMenu()
        self.emp_form = employee_form.EmployeeForm()

    def createMenu(self):
        menu = self.menuBar().addMenu("&File")
        menu.addAction("&Add new employee", self.open_employee_form)
        menu.addAction("&Refresh table", self.populate_table)
        menu.addAction("&Exit", self.close)

    def open_employee_form(self):
        self.emp_form.show()

    def populate_table(self):
        emp_dao = employee_dao.EmployeeDAO()
        data = emp_dao.getAllEmployees()
        print('data', data)

        if len(data['Name']) > 0:
            self.table = table_view.TableView(data, len(data['Name']), 3)
            self.setCentralWidget(self.table)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
