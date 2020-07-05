from main_windows import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot

from main_simplex import SimplexWin
from main_affectation import MainAffectation
from main_transport import TransportWin

import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

    
    @pyqtSlot()
    def on_pushButtonTransport_clicked(self):
        win = TransportWin()
        win.exec_()

    
    @pyqtSlot()
    def on_pushButtonAffectation_clicked(self):
        win = MainAffectation()
        win.exec_()

    @pyqtSlot()
    def on_pushButtonSimplex_clicked(self):
        win = SimplexWin()
        win.exec_()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
