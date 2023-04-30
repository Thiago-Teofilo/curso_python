from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget, QLineEdit

class MainWin(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gLayout = QGridLayout()
        self.cw = QWidget()

        self.setCentralWidget(self.cw)
        self.cw.setLayout(self.gLayout)

        self.input = QLineEdit()

        self.gLayout.addWidget(self.input)