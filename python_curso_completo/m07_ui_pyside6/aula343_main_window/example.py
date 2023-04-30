import sys
from PySide6.QtWidgets import (QApplication, QPushButton, 
                               QWidget, QGridLayout, 
                               QMainWindow)

def choice_color_button(button):
    button.setStyleSheet("background-color: red;")

my_app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
layout = QGridLayout()

window.setCentralWidget(central_widget)
central_widget.setLayout(layout)

botao = QPushButton("Botão")
botao.setStyleSheet('font-size: 50px;')
layout.addWidget(botao)

status_bar = window.statusBar()
status_bar.showMessage("App carregado com sucesso!")

menu_bar = window.menuBar()
nav1 = menu_bar.addMenu("Navegação")
action1 = nav1.addAction("Ação")
action1.triggered.connect(
    lambda: choice_color_button(botao)
    )

window.show()
my_app.exec()