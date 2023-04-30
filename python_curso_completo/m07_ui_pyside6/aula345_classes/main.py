# Documentação
# https://doc.qt.io/qtforpython-6/index.html

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton ,QWidget, 
                               QGridLayout, QMainWindow)

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Botão 1
        self.botao1 = QPushButton('Texto do botão')
        self.botao1.setStyleSheet('font-size: 80px;')
        self.botao1.clicked.connect(self.outro_slot)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela')

        self.botao2 = QPushButton('Botão 2')
        self.botao2.setStyleSheet('font-size: 40px')

        self.botao3 = QPushButton('Botão 3')
        self.botao3.setStyleSheet('font-size: 40px')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem')

        # menuBar
        self.menu = self.menuBar()

        self.primeiro_menu = self.menu.addMenu('Primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeira_acao.triggered.connect(self.slot_example())

        self.segunda_acao = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.outro_slot)
        self.segunda_acao.hovered.connect(self.outro_slot)

    @Slot()
    def slot_example(self):
        self.status_bar.showMessage("O meu slot foi executado")

    @Slot()
    def outro_slot(self):
        print('Está marcado?', self.segunda_acao.isChecked())
    
app = QApplication(sys.argv)
window = MyWindow()

window.show()
app.exec()