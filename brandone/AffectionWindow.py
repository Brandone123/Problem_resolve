# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'affectation.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(732, 518)
        Form.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.spinBoxCol = QtWidgets.QSpinBox(Form)
        self.spinBoxCol.setFrame(True)
        self.spinBoxCol.setObjectName("spinBoxCol")
        self.horizontalLayout_3.addWidget(self.spinBoxCol)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spinBoxRow = QtWidgets.QSpinBox(Form)
        self.spinBoxRow.setObjectName("spinBoxRow")
        self.horizontalLayout_3.addWidget(self.spinBoxRow)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButtonGenMatrix = QtWidgets.QPushButton(Form)
        self.pushButtonGenMatrix.setObjectName("pushButtonGenMatrix")
        self.verticalLayout.addWidget(self.pushButtonGenMatrix)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayoutMatrix = QtWidgets.QVBoxLayout()
        self.verticalLayoutMatrix.setObjectName("verticalLayoutMatrix")
        self.verticalLayout.addLayout(self.verticalLayoutMatrix)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.labelResult = QtWidgets.QLabel(Form)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.horizontalLayout_2.addWidget(self.labelResult)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Problème d\'affectation"))
        self.label.setText(_translate("Form", "Entrez la taille de la matrice à genérer : "))
        self.label_2.setText(_translate("Form", "X"))
        self.pushButtonGenMatrix.setText(_translate("Form", "Generer la matrice"))

