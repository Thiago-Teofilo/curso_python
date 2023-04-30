import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton ,QWidget, 
                               QGridLayout, QMainWindow)

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.central_widget = QWidget()
        self.grid_layout = QGridLayout()

        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)
        
        # Make Buttons:
        self.button1 = self.mk_button("Excute count")
        self.grid_layout.addWidget(self.button1)
        self.button1.clicked.connect(self.execute_count)
        
        self.status_bar = self.statusBar()
        self.menu_bar = self.menuBar() 

        self.menu = self.menu_bar.addMenu("Mode")

        self.rage_mode = self.menu.addAction("Rage mode")
        self.rage_mode.setCheckable(True)
        self.rage_mode.toggled.connect(self.on_rage_mode)
    
    def mk_button(self, text: str):
        button = QPushButton(text)
        button.setStyleSheet(
            """
            font-size: 22px;
            padding: 20px 40px;
            """
        )
        return button
    
    @Slot()
    def on_rage_mode(self):
        if self.rage_mode.isChecked() is True:
            self.button1.setStyleSheet(
                """
                background-color: red;
                font-size: 22px;
                padding: 20px 40px;
                """
            )
        else:
            self.button1.setStyleSheet(
                """
                background-color: white;
                font-size: 22px;
                padding: 20px 40px;
                """
            )

    @Slot()
    def execute_count(self):
        [print(x) for x in range(10)]

app = QApplication(sys.argv)
main = MyWindow()

main.show()
app.exec()