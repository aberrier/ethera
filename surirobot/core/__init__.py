import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from .gui.ui import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.smartShow()
