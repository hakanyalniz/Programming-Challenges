from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QMessageBox
import json


# Subclass QMainWindow to customize applications main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        mainLayout = QVBoxLayout()
        central_widget.setLayout(mainLayout)

        # set the title, resize and make it central
        self.setWindowTitle("To-Do List")
        self.setMinimumSize(QSize(400, 300))    

        # build the widgets
        self.buildWidgets(mainLayout)

    
    def buildWidgets(self, mainLayout):
        
        # create a list widget
        self.myList = QListWidget()
        mainLayout.addWidget(self.myList)

        # Create a QLineEdit for task input
        self.taskInput = QLineEdit()
        self.taskInput.setPlaceholderText("Enter a task...")
        mainLayout.addWidget(self.taskInput)

        # create horizontal layout for buttons
        button_layout = QHBoxLayout()
        mainLayout.addLayout(button_layout)

        # Create a QPushButton to add tasks
        self.addButton = QPushButton("Add Task")
        self.addButton.clicked.connect(self.addTask)
        self.addButton.setFixedSize(QSize(100, 30))
        button_layout.addWidget(self.addButton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Delete tasks
        self.addButton = QPushButton("Delete Task")
        self.addButton.clicked.connect(self.deleteTask)
        self.addButton.setFixedSize(QSize(100, 30))
        button_layout.addWidget(self.addButton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Export tasks
        self.addButton = QPushButton("Export")
        self.addButton.clicked.connect(self.exportList)
        self.addButton.setFixedSize(QSize(100, 30))
        button_layout.addWidget(self.addButton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Import tasks
        self.addButton = QPushButton("Import")
        self.addButton.clicked.connect(self.importList)
        self.addButton.setFixedSize(QSize(100, 30))
        button_layout.addWidget(self.addButton, alignment=Qt.AlignmentFlag.AlignCenter)


    # add the entered task to list 
    def addTask(self, importTaskText = 0, importTaskCheck = 0):
        # Get the task from the QLineEdit
        # if importing, get the import text instead
        if (importTaskText != 0):
            task = importTaskText  
        else:
            task = self.taskInput.text()  
           
        # Check if the input is not empty
        if task: 
            # Add the task to the QListWidget
            self.myList.addItem(task) 
            # Clear the input field 
            self.taskInput.clear()
        
        # make sure the list is populated, or else the count below will give error
        # if importing, instead of adding check as unchecked, make it follow the import
        if (self.myList.count() > 0):
            # make item editable and add check
            lastItem = self.myList.item(self.myList.count() - 1)
            lastItem.setFlags(lastItem.flags() | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsUserCheckable)  
            # importTaskCheck is either true or false
            # if true, checked, otherwise false 
            if (importTaskCheck != 0):
                lastItem.setCheckState(Qt.CheckState.Checked)
            else:
                lastItem.setCheckState(Qt.CheckState.Unchecked)


    # delete task when clicked
    def deleteTask(self):
        selectedItems = self.myList.selectedItems()
        if not selectedItems: return
        # if it exists, delete it
        for item in selectedItems:
            self.myList.takeItem(self.myList.row(item))


    # export to json after getting file location from user
    def exportList(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "JSON Files (*.json);;TXT Files(*.txt);;All Files (*)")
        tasks = []
        for index in range(self.myList.count()):
            item = self.myList.item(index)
            tasks.append({
            "text": item.text(),
            "checked": item.checkState() == Qt.CheckState.Checked})

        with open(file_path, "w") as file:
            json.dump(tasks, file)
    

    # delete current list, import the new one
    def importList(self):
        reply = QMessageBox.warning(self, "Warning", "Importing will clear all of your current tasks. Do you want to continue?", 
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No);  
        # if the user says no, then return without doing anything
        if (reply == QMessageBox.StandardButton.No):
            return 0
        file_path, _ = QFileDialog.getOpenFileName(self, "Save File", "", "JSON Files (*.json);;TXT Files(*.txt);;All Files (*)")

        # check if file path is cancelled
        if (file_path != ''):
            self.myList.clear()

            with open(file_path, "r") as file:
                tasks = json.load(file)

            # for each item in json, call addTask to add them
            for index in range(0, len(tasks)):
                self.addTask(tasks[index]["text"], tasks[index]["checked"])


def main():
    # only one of QApplication is required
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()