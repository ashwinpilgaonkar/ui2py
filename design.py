# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/AndroidApps/ui2py/UI/design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ui2py(object):
    def setupUi(self, ui2py):
        ui2py.setObjectName("ui2py")
        ui2py.resize(445, 260)
        ui2py.setMinimumSize(QtCore.QSize(445, 260))
        self.centralwidget = QtWidgets.QWidget(ui2py)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.OpenButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenButton.setObjectName("OpenButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.OpenButton)
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setObjectName("SaveButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.SaveButton)
        self.PathLabel = QtWidgets.QLabel(self.centralwidget)
        self.PathLabel.setObjectName("PathLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.PathLabel)
        ui2py.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ui2py)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 445, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        ui2py.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ui2py)
        self.statusbar.setObjectName("statusbar")
        ui2py.setStatusBar(self.statusbar)
        self.actionUsage = QtWidgets.QAction(ui2py)
        self.actionUsage.setObjectName("actionUsage")
        self.actionInfo = QtWidgets.QAction(ui2py)
        self.actionInfo.setObjectName("actionInfo")
        self.menuHelp.addAction(self.actionUsage)
        self.menuAbout.addAction(self.actionInfo)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(ui2py)
        QtCore.QMetaObject.connectSlotsByName(ui2py)

    def retranslateUi(self, ui2py):
        _translate = QtCore.QCoreApplication.translate
        ui2py.setWindowTitle(_translate("ui2py", "ui2py"))
        self.OpenButton.setText(_translate("ui2py", "Open"))
        self.SaveButton.setText(_translate("ui2py", "Convert"))
        self.PathLabel.setText(_translate("ui2py", "No files selected"))
        self.menuHelp.setTitle(_translate("ui2py", "Help"))
        self.menuAbout.setTitle(_translate("ui2py", "About"))
        self.actionUsage.setText(_translate("ui2py", "Usage"))
        self.actionInfo.setText(_translate("ui2py", "Info"))

