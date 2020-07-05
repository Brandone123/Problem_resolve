from PyQt5.QtWidgets import QDialog, QMessageBox, QSpacerItem, QPushButton, QSpinBox, QHBoxLayout, QApplication
# from PyQt5.QtGui import Q
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from munkres import Munkres, print_matrix

from TransportWindow import Ui_Form
from transport import nw_algorithm_calculation, bh_algorithm_calculation
import sys


class TransportWin(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        # self.label_3.setText("Algo probleme de transport")

        self.matrix_cost = []
        self.send_quantities = []
        self.receive_quantities = []
        
    @pyqtSlot()
    def on_pushButtonGenMatrix_clicked(self):
        col = self.spinBoxCol.value()
        row = self.spinBoxRow.value()

        self.create_matrix(row, col)

    def create_matrix(self, row, col):
        for i in range(1, row + 1):
            r = []
            hLayout = QHBoxLayout()
            for j in range(1, col+1):
                spin = QSpinBox()
                spin.setObjectName('spinBox_{}_{}'.format(i, j))
                spin.setMinimum(-1000)
                spin.setMaximum(1000)
                hLayout.addWidget(spin)
                
                r.append(spin)
            
            spinReceive = QSpinBox()
            spinReceive.setMinimum(-1000)
            spinReceive.setMaximum(1000)
            self.receive_quantities.append(spinReceive)

            hLayout.addWidget(spinReceive)
            
            self.matrix_cost.append(r)
            self.verticalLayoutMatrix.addLayout(hLayout)

        sendLayout = self.create_send_quantities_layout(col)
        self.verticalLayoutMatrix.addLayout(sendLayout)

        pushButtonCompute = QPushButton('Compute')
        pushButtonCompute.clicked.connect(self.compute_transport)
        self.verticalLayoutMatrix.addWidget(pushButtonCompute)

    def get_matrix(self):
        matrix = []
        for row in self.matrix_cost:
            _row = []
            for col in row:
                _row.append(col.value())
            matrix.append(_row)
    
        return matrix

    
    def get_send(self, quantities):
        return [ entry.value() for entry in quantities ]

    def compute_transport(self):
        matrix = self.get_matrix()
        send_qte = self.get_send(self.send_quantities)
        receive_qte = self.get_send(self.receive_quantities)
        method = 'NW' if self.radioButtonNW.isChecked() else 'BH'
        result = self.make_calculation(matrix, send_qte, receive_qte, method)

        self.labelResult.setText(result)

    def make_calculation(self, matrix, send_qte, receive_qte, method):
        methods = {'NW': nw_algorithm_calculation, 'BH': bh_algorithm_calculation}
        path, cost = methods[method](matrix, send_qte, receive_qte)

        return 'Chemin : {} \n Cout : {}'.format(path, cost)

    def create_send_quantities_layout(self, col):
        hLayout = QHBoxLayout()
        
        for i in range(1, col+1):
            spin = QSpinBox()
            spin.setMinimum(-1000)
            spin.setMaximum(1000)
            spin.setObjectName('spin_{}'.format(i))
            self.send_quantities.append(spin)

            hLayout.addWidget(spin)

        hLayout.addItem(QSpacerItem(20,20))

        return hLayout
    