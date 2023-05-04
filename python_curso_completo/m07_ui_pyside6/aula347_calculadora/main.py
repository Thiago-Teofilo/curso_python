import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from main_window import MainWindow
from display import Display
from buttons import Button, ButtonsGrid
from info import Info
from styles import setupTheme

from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    #Cria aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)
    
    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa aplicação
    window.adjustFixedSize()
    window.show()
    app.exec()