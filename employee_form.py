from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QWidget
import employee_dao
import employee


class EmployeeForm(QWidget):
    """
    The EmployeeForm class.
    """
    def __init__(self):
        super().__init__()

        self.name = QLineEdit()
        self.name.setObjectName("name")

        self.age = QLineEdit()
        self.age.setObjectName("age")

        self.phone = QLineEdit()
        self.phone.setObjectName("phone")

        layout = QFormLayout()
        layout.addRow("Name:", self.name)
        layout.addRow("Age:", self.age)
        layout.addRow("Phone:", self.phone)
        self.button = QPushButton()
        self.button.setObjectName("save")
        self.button.setText("Save")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.create_employee)
        self.setLayout(layout)

    def create_employee(self):
        emp = employee.Employee(self.name.text(), self.age.text(), self.phone.text())
        emp_dao = employee_dao.EmployeeDAO()
        if emp_dao.createEmployee(emp):
            self.name.setText(None)
            self.age.setText(None)
            self.phone.setText(None)
            self.close()
            return True

        return False


