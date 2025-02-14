from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QLineEdit, QPushButton, QVBoxLayout, QWidget


# Subclass QMainWindow to customize applications main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # set the title, resize and make it central
        self.setWindowTitle("To-Do List")
        self.setMinimumSize(QSize(400, 300))

        # create a list widget
        self.myList = QListWidget()
        layout.addWidget(self.myList)

        # Create a QLineEdit for task input
        self.taskInput = QLineEdit()
        self.taskInput.setPlaceholderText("Enter a task...")
        layout.addWidget(self.taskInput)

        # Create a QPushButton to add tasks
        self.addButton = QPushButton("Add Task")
        self.addButton.clicked.connect(self.addTask)
        self.addButton.setFixedSize(QSize(100, 30))
        layout.addWidget(self.addButton, alignment=Qt.AlignmentFlag.AlignCenter)

    
    def addTask(self, task):
        # Get the task from the QLineEdit
        task = self.taskInput.text()  
        # Check if the input is not empty
        if task: 
            # Add the task to the QListWidget
            self.myList.addItem(task) 
            # Clear the input field 
            self.taskInput.clear()  

def main():
    # only one of QApplication is required
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()