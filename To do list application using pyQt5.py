import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QAbstractItemView
from PyQt5.QtCore import Qt

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('To-Do List App')
        self.setGeometry(100, 100, 500, 400)

        
        self.init_ui()

    def init_ui(self):
       
        layout = QVBoxLayout()

     
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText('Enter new task')

       
        self.add_button = QPushButton('Add Task', self)
        self.add_button.clicked.connect(self.add_task)

     
        self.delete_button = QPushButton('Delete Task', self)
        self.delete_button.clicked.connect(self.delete_task)

       
        self.mark_button = QPushButton('Mark as Completed', self)
        self.mark_button.clicked.connect(self.mark_completed)

     
        self.task_list = QListWidget(self)
        self.task_list.setSelectionMode(QAbstractItemView.SingleSelection)

       
        layout.addWidget(self.task_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.mark_button)
        layout.addWidget(self.task_list)

        self.setLayout(layout)

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            row = self.task_list.row(item)
            self.task_list.takeItem(row)

    def mark_completed(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            item.setText(item.text() + " (Completed)")
            item.setBackground(Qt.green)  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec_())
