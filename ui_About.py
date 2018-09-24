# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/About.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 156)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.verticalLayout.addWidget(self.groupBox)
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setObjectName("btnOK")
        self.verticalLayout.addWidget(self.btnOK)

        self.retranslateUi(Dialog)
        self.btnOK.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.groupBox.setTitle(_translate("Dialog", "About potrace GUI"))
        self.label.setText(_translate("Dialog", "Author"))
        self.label_2.setText(_translate("Dialog", "@MizunagiKB"))
        self.label_3.setText(_translate("Dialog", "Web site"))
        self.label_4.setText(_translate("Dialog", "https://www.mizunagi-works.com/wp/"))
        self.btnOK.setText(_translate("Dialog", "OK"))

