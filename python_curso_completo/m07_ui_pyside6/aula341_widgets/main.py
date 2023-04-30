# Documentação
# https://doc.qt.io/qtforpython-6/index.html

import sys
from PySide6.QtWidgets import QApplication, QPushButton ,QWidget, QGridLayout

app = QApplication(sys.argv)
central_widget = QWidget()
layout = QGridLayout()
central_widget.setLayout(layout)


botao1 = QPushButton('Botão 1')
botao1.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px')

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


central_widget.show()
app.exec()