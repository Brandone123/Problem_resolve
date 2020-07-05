from PyQt5.QtWidgets import QDialog, QMessageBox, QSpacerItem, QPushButton, QSpinBox, QHBoxLayout, QApplication
# from PyQt5.QtGui import Q
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from munkres import Munkres, print_matrix

from AffectionWindow import Ui_Form

import sys


class MainAffectation(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.cell_list = []

    @pyqtSlot()
    def on_pushButtonGenMatrix_clicked(self):
        col = self.spinBoxCol.value()
        row = self.spinBoxRow.value()

        self.create_matrix_row(col, row)

    def create_matrix_row(self, row, col):
        for i in range(1, row+1):
            hLayout = QHBoxLayout()
            hSpacer = QSpacerItem(40, 20)
            hLayout.addItem(hSpacer)
            row_list = []
            for j in range(1, col+1):
                spinBox = QSpinBox()
                object_name = 'spinBox_{}_{}'.format(i, j)
                row_list.append(spinBox)
                spinBox.setObjectName(object_name)
                spinBox.setMinimum(-999)
                spinBox.setMaximum(999)
                hLayout.addWidget(spinBox)
            self.cell_list.append(row_list)
            hLayout.addItem(hSpacer)
            self.verticalLayoutMatrix.addLayout(hLayout)

        verticalSpacer = QSpacerItem(20, 40)

        self.verticalLayoutMatrix.addItem(verticalSpacer)
        pushButtonCompute = QPushButton('Compute')
        self.verticalLayoutMatrix.addWidget(pushButtonCompute)

        pushButtonCompute.clicked.connect(self.compute_affectation)

    def compute_affectation(self):
        matrix = self.get_matrix(self.cell_list)
        munkres = Munkres()
        indexes = munkres.compute(matrix)

        display_result = 'Resultat : {} \n Cout : {}'.format(
            str(indexes), sum([matrix[i[1]][i[next]] for i in indexes]))
        self.labelResult.setText(str(display_result))

    def get_matrix(self, cell_list):
        matrix = []
        for row in cell_list:
            m_row = []
            for col in row:
                m_row.append(col.value())
            matrix.append(m_row)
        return matrix
