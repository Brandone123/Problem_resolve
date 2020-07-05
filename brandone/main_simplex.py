from PyQt5.QtWidgets import (
    QDialog, QMessageBox, 
    QSpacerItem, QPushButton, 
    QSpinBox, QHBoxLayout, 
    QApplication, QLabel, QComboBox)

# from PyQt5.QtGui import Q
from PyQt5.QtCore import pyqtSlot

from PyQt5 import QtGui
from munkres import Munkres, print_matrix
import sys
from SimplexWindow import Ui_Form

from simplex import gen_matrix, constrain, obj, maxz, minz

class SimplexWin(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.cell_list = []
        self.constrains = []
        self.objectif_func = []
        # self.label_3.setText('Simplex')
        self.matrix = []
        self.pushButtonGenerate.clicked.connect(self.on_pushButtonGenerate)

    def on_pushButtonGenerate(self):
        v = self.spinBoxVariables.value()
        c = self.spinBoxConstantes.value()
        self.create_constrain(v, c)

    def create_constrain(self, v, c):
        for i in range(1, c + 1):
            variables = []
            hLayout = QHBoxLayout()
            hLayout.addWidget(QLabel('Contrainte {}'.format(i)))

            for j in range(1, v + 1):
                spinBox = QSpinBox()
                spinBox.setObjectName('spinBox_{}_{}'.format(i,j))
                spinBox.setMinimum(-999)
                spinBox.setMaximum(999)
                variables.append(spinBox)
                hLayout.addWidget(spinBox)

            combo = QComboBox()
            combo.addItem('L')
            combo.addItem('G')
            
            spinBoxC = QSpinBox()
            spinBoxC.setMinimum(-99)

            variables.append(combo)
            variables.append(spinBoxC)

            hLayout.addWidget(combo)
            hLayout.addWidget(spinBoxC)

            self.constrains.append(variables)
            self.verticalLayoutConstrains.addLayout(hLayout)

        pushButtonCompute = QPushButton('Compute')
        pushButtonCompute.clicked.connect(self.compute_simplex)

        obj_layout = self.create_objectif(v)
        self.verticalLayoutConstrains.addLayout(obj_layout)
        spacer = QSpacerItem(20,20)
        self.verticalLayoutConstrains.addItem(spacer)
        self.verticalLayoutConstrains.addWidget(pushButtonCompute)

        self.matrix = gen_matrix(v, c)


    def create_objectif(self, v):
        hLayout = QHBoxLayout()
        hLayout.addWidget(QLabel('Fonction Objectif :'))
        for i in range(1, v+1):
            spinBox = QSpinBox()
            spinBox.setObjectName('spinBoxObj_{}'.format(i))
            spinBox.setMinimum(-99)
            hLayout.addWidget(spinBox)
            self.objectif_func.append(spinBox)

        spinBox = QSpinBox()
        spinBox.setObjectName('spinBoxObjConstante')
        self.objectif_func.append(spinBox)
        hLayout.addWidget(spinBox)

        return hLayout

    def get_constrains(self, constrains_list):
        constrains = []
        for c in constrains_list:
            rules = []
            for rule in c:
                if isinstance(rule, QComboBox):
                    rules.append(rule.currentText())
                    continue
                rules.append(str(rule.value()))
            constrains.append(rules)
        
        constrains = [ ','.join(c) for c in constrains ]

        return constrains

    def get_objectif(self, objectif_list): 
        objectif = ','.join([ str(spin.value()) for spin in objectif_list ])
        return objectif

    def compute_simplex(self):
        constrains = self.get_constrains(self.constrains)   
        objectif = self.get_objectif(self.objectif_func)     
        result = self.make_calculation(self.matrix, constrains, objectif)

        self.labelResult.setText(str(result))

    def make_calculation(self, matrix, constrains, objectif):
        matrix = matrix
        for c in constrains:
            constrain(matrix, c)
        
        obj(matrix, objectif)

        if self.comboBoxMaxMin.currentText() == 'Maximiser':
            return maxz(matrix)
        return minz(matrix)
