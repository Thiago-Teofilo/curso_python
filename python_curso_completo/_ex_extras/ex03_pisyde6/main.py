from PySide6.QtWidgets import QApplication
import sys

from main_window import MainWin

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWin()

    main_win.show()
    app.exec()