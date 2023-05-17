from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, QThread, Signal, Slot

import time
import sys

from worker_ui import Ui_myWidget


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWork(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    @Slot()
    def hardWork1(self):
        self._worker1 = Worker1()
        self._thread1 = QThread()

        worker = self._worker1
        thread = self._thread1
        
        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        thread.start()

    def worker1Started(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print("Worker iniciado")

    def worker1Progressed(self, value):
        self.label1.setText(value)
        print("Worker em progresso")

    def worker1Finished(self, value):
        self.button1.setDisabled(False)
        self.label1.setText(value)
        print("Worker finalizado")

    @Slot()
    def hardWork2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2
        
        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)

        thread.start()

    def worker2Started(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print("Worker iniciado")

    def worker2Progressed(self, value):
        self.label2.setText(value)
        print("Worker em progresso")

    def worker2Finished(self, value):
        self.button2.setDisabled(False)
        self.label2.setText(value)
        print("Worker finalizado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = MyWidget()

    myWidget.show()
    app.exec()