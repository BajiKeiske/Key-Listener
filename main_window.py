from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QSize, Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Key listener')
        self.setFixedSize(QSize(600, 400))


app = QApplication(sys.argv)

window = MainWindow()
window.show()