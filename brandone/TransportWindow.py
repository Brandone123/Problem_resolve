# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transport.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(662, 471)
        Form.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBoxRow = QtWidgets.QSpinBox(Form)
        self.spinBoxRow.setObjectName("spinBoxRow")
        self.horizontalLayout.addWidget(self.spinBoxRow)
        self.spinBoxCol = QtWidgets.QSpinBox(Form)
        self.spinBoxCol.setObjectName("spinBoxCol")
        self.horizontalLayout.addWidget(self.spinBoxCol)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.radioButtonNW = QtWidgets.QRadioButton(Form)
        self.radioButtonNW.setChecked(True)
        self.radioButtonNW.setObjectName("radioButtonNW")
        self.horizontalLayout.addWidget(self.radioButtonNW)
        self.radioButtonBH = QtWidgets.QRadioButton(Form)
        self.radioButtonBH.setAutoExclusive(True)
        self.radioButtonBH.setObjectName("radioButtonBH")
        self.horizontalLayout.addWidget(self.radioButtonBH)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButtonGenMatrix = QtWidgets.QPushButton(Form)
        self.pushButtonGenMatrix.setObjectName("pushButtonGenMatrix")
        self.verticalLayout.addWidget(self.pushButtonGenMatrix)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayoutMatrix = QtWidgets.QVBoxLayout()
        self.verticalLayoutMatrix.setObjectName("verticalLayoutMatrix")
        self.horizontalLayout_2.addLayout(self.verticalLayoutMatrix)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.labelResult = QtWidgets.QLabel(Form)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout.addWidget(self.labelResult)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Transport Balas Hammer & Nord-Ouest"))
        self.label_2.setText(_translate("Form", "Entrez la taille de la matrice :"))
        self.label_3.setText(_translate("Form", "Methode :"))
        self.radioButtonNW.setText(_translate("Form", "NW"))
        self.radioButtonBH.setText(_translate("Form", "BH"))
        self.pushButtonGenMatrix.setText(_translate("Form", "Generer la matrice"))

